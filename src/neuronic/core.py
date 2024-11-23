from typing import Union, Any
import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from enum import Enum
from diskcache import Cache
import tempfile


class NeuronicError(Exception):
    """Base exception for Neuronic errors."""

    pass


class APIKeyError(NeuronicError):
    """Raised when there are issues with the API key."""

    pass


class TransformationError(NeuronicError):
    """Raised when transformation fails."""

    pass


class OutputType(Enum):
    STRING = "string"
    NUMBER = "number"
    JSON = "json"
    LIST = "list"
    BOOL = "bool"
    PYTHON = "python"


class Neuronic:
    """
    AI-powered data transformation and analysis tool.
    Converts, analyzes, and generates data in various formats.
    """

    def __init__(
        self, 
        api_key: str = None, 
        model: str = "gpt-3.5-turbo", 
        cache_dir: str = None,
        cache_ttl: int = 3600
    ):
        """
        Initialize Neuronic with OpenAI API key and optional caching settings.

        Args:
            api_key: OpenAI API key. If None, will look for OPENAI_API_KEY in environment
            model: OpenAI model to use for completions
            cache_dir: Directory to store cache. If None, uses system temp directory
            cache_ttl: Time to live for cached results in seconds (default: 1 hour)
        """
        load_dotenv()
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise APIKeyError(
                "OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass to constructor."
            )

        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        
        # Initialize disk cache
        cache_dir = cache_dir or os.path.join(tempfile.gettempdir(), 'neuronic_cache')
        self.cache = Cache(cache_dir)
        self.cache_ttl = cache_ttl

    def _parse_output(self, result: str, output_type: OutputType) -> Any:
        """Parse the output string based on desired type."""
        try:
            if output_type == OutputType.JSON or output_type == OutputType.LIST or output_type == OutputType.PYTHON:
                return json.loads(result)
            if output_type == OutputType.NUMBER:
                return float(result.replace(",", ""))
            if output_type == OutputType.BOOL:
                return result.lower() in ("true", "yes", "1", "y")
            return str(result)
        except Exception as e:
            raise TransformationError(f"Could not convert response to {output_type.value}: {str(e)}")

    def _get_cache_key(self, data: Any, instruction: str, output_type: OutputType, context: dict = None) -> str:
        """Generate a unique cache key for the request."""
        context_str = json.dumps(context) if context else ""
        return f"{str(data)}|{instruction}|{output_type.value}|{context_str}"

    def transform(
        self,
        data: Any,
        instruction: str,
        output_type: Union[OutputType, str] = OutputType.STRING,
        example: str = None,
        context: dict = None,
        use_cache: bool = True,
    ) -> Any:
        """
        Transform data according to instructions.

        Args:
            data: Input data to transform
            instruction: What to do with the data
            output_type: Desired output format (OutputType enum or string)
            example: Optional example of desired output
            context: Optional dictionary of context information
            use_cache: Whether to use cached results (default: True)
        """
        # Convert string output_type to enum
        if isinstance(output_type, str):
            try:
                output_type = OutputType(output_type.lower())
            except ValueError:
                valid_types = ", ".join(t.value for t in OutputType)
                raise ValueError(
                    f"Invalid output_type: {output_type}. Must be one of: {valid_types}"
                )

        # Check cache if enabled
        if use_cache:
            cache_key = self._get_cache_key(data, instruction, output_type, context)
            if cache_key in self.cache:
                return self.cache[cache_key]

        # Build the prompt
        prompt = "\n".join([
            f"Instruction: {instruction}",
            f"Input Data: {data}",
            f"Desired Format: {output_type.value}",
            f"Context: {json.dumps(context)}" if context else "",
            f"Example Output: {example}" if example else "",
            "\nOutput (in JSON format):"
        ])

        messages = [
            {
                "role": "system",
                "content": "You are a data transformation expert. Process the input according to instructions and return in the exact format specified. Only return the processed output, nothing else.",
            },
            {"role": "user", "content": prompt}
        ]

        try:
            # Get completion from OpenAI using the new API
            response = self.client.chat.completions.create(
                model=self.model, messages=messages, temperature=0.3, max_tokens=500
            )

            result = response.choices[0].message.content.strip()
            parsed_result = self._parse_output(result, output_type)

            # Cache the result if caching is enabled
            if use_cache:
                self.cache.set(cache_key, parsed_result, expire=self.cache_ttl)

            return parsed_result

        except Exception as e:
            raise TransformationError(f"OpenAI API error: {str(e)}")

    def analyze(self, data: Any, question: str) -> dict:
        """
        Analyze data and answer questions about it.

        Args:
            data: Data to analyze
            question: Question about the data

        Returns:
            Dictionary containing analysis results with keys:
            - answer: Detailed answer to the question
            - confidence: Confidence score (0-1)
            - reasoning: Explanation of the analysis

        Raises:
            TransformationError: If analysis fails
        """
        return self.transform(
            data=data,
            instruction=f"Analyze this data and answer: {question}",
            output_type=OutputType.JSON,
            example='{"answer": "detailed answer", "confidence": 0.85, "reasoning": "explanation"}',
        )

    def generate(self, spec: str, n: int = 1) -> list:
        """
        Generate new data based on specifications.

        Args:
            spec: Specification of what to generate
            n: Number of items to generate

        Returns:
            List of generated items

        Raises:
            TransformationError: If generation fails
            ValueError: If n < 1
        """
        if n < 1:
            raise ValueError("Number of items to generate must be at least 1")

        return self.transform(
            data=f"Generate {n} items",
            instruction=spec,
            output_type=OutputType.LIST,
            context={"count": n},
        )
