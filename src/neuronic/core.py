from typing import Union, Literal, Any
import os
from openai import OpenAI
from dotenv import load_dotenv
import json


class NeuronicError(Exception):
    """Base exception for Neuronic errors."""

    pass


class APIKeyError(NeuronicError):
    """Raised when there are issues with the API key."""

    pass


class TransformationError(NeuronicError):
    """Raised when transformation fails."""

    pass


class Neuronic:
    """
    AI-powered data transformation and analysis tool.
    Converts, analyzes, and generates data in various formats.
    """

    OUTPUT_TYPES = Literal["string", "number", "json", "list", "bool", "python"]

    def __init__(self, api_key: str = None, model: str = "gpt-3.5-turbo"):
        """
        Initialize with OpenAI API key from env or direct input.

        Args:
            api_key: OpenAI API key. If None, will look for OPENAI_API_KEY in environment
            model: OpenAI model to use for completions

        Raises:
            APIKeyError: If no API key is provided or found in environment
        """
        load_dotenv()
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise APIKeyError(
                "OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass to constructor."
            )

        self.model = model
        self.client = OpenAI(api_key=self.api_key)

    def _parse_output(self, result: str, output_type: OUTPUT_TYPES) -> Any:
        """Parse the output string based on desired type."""
        try:
            # Ensure the result is parsed as JSON if structured output is expected
            if output_type in ["json", "list", "python"]:
                return json.loads(result)
            elif output_type == "number":
                return float(result.replace(",", ""))
            elif output_type == "bool":
                return result.lower() in ("true", "yes", "1", "y")
            else:
                return str(result)
        except Exception as e:
            raise TransformationError(
                f"Could not convert response to {output_type}: {str(e)}"
            )

    def transform(
        self,
        data: Any,
        instruction: str,
        output_type: OUTPUT_TYPES = "string",
        example: str = None,
        context: dict = None,
    ) -> Any:
        """
        Transform data according to instructions.

        Args:
            data: Input data to transform (can be any type)
            instruction: What to do with the data
            output_type: Desired output format
            example: Optional example of desired output
            context: Optional dictionary of context information

        Returns:
            Transformed data in specified format

        Raises:
            TransformationError: If transformation fails
        """
        # Build the prompt
        messages = [
            {
                "role": "system",
                "content": "You are a data transformation expert. Process the input according to instructions and return in the exact format specified. Only return the processed output, nothing else.",
            },
        ]

        # Enforce structured output
        prompt = f"""
Instruction: {instruction}
Input Data: {data}
Desired Format: {output_type}
"""
        if context:
            prompt += f"\nContext: {json.dumps(context)}"
        if example:
            prompt += f"\nExample Output: {example}"

        # Add a clear structure to the output
        prompt += "\n\nOutput (in JSON format):"

        messages.append({"role": "user", "content": prompt})

        try:
            # Get completion from OpenAI using the new API
            response = self.client.chat.completions.create(
                model=self.model, messages=messages, temperature=0.3, max_tokens=500
            )

            result = response.choices[0].message.content.strip()
            return self._parse_output(result, output_type)

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
            output_type="json",
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
            output_type="list",
            context={"count": n},
        )
