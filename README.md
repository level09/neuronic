# Neuronic 

<p align="center">
  <img src="https://raw.githubusercontent.com/level09/neuronic/main/.github/images/neuronic.png" alt="Neuronic Logo" width="440"/>
</p>

Imagine Python functions that can think, reason, and create - functions that understand natural language, analyze complex data patterns, and generate creative solutions. Welcome to Neuronic - where we transform ordinary Python code into intelligent, AI-powered modules that bring GPT's cognitive capabilities directly into your codebase, complete with enterprise-grade validation, caching, and error handling.

## 🌟 What is Neuronic?

Neuronic is your gateway to building intelligent Python applications powered by GPT. Create functions that can understand context, extract insights, and solve complex problems - all while maintaining the reliability and predictability of traditional programming. With built-in validation, type checking, and caching, Neuronic makes AI as dependable as any other Python module.

## 🚀 Features

- **Intelligent Understanding:** Create functions that truly understand your data, extracting meaning and insights
- **Natural Language Processing:** Process text like a human - analyze sentiment, extract key information, and understand context
- **Creative Generation:** Generate human-quality content, from documentation to test data, tailored to your specifications
- **Pattern Recognition:** Uncover hidden patterns and relationships in your data through GPT-powered analysis
- **Context-Aware Intelligence:** Leverage surrounding context for more nuanced and accurate processing
- **Multiple Output Types:** Get results in any format you need - strings, numbers, JSON, lists, booleans, or Python structures
- **Enterprise Reliability:** Built-in validation and type checking ensure predictable, production-ready outputs

## Installation

Install using pip:

    pip install neuronic

## Configuration

Create a `.env` file in your project root:

    OPENAI_API_KEY=your-openai-api-key-here

Or pass your API key directly:

    neuronic = Neuronic(api_key="your-api-key-here")

## Usage Examples

### 1. Data Transformation

Convert CSV data to JSON format:

    from neuronic import Neuronic
    
    neuronic = Neuronic()
    
    customer_data = "John Doe, john@example.com, New York"
    contact_card = neuronic.transform(
        data=customer_data,
        instruction="Convert this CSV data into a contact card format",
        output_type="json",
        example='{"name": "Jane Doe", "email": "jane@example.com", "location": "Los Angeles"}'
    )

### 2. Data Analysis

Analyze sales data and get insights:

    sales_data = [
        {"month": "Jan", "revenue": 1000},
        {"month": "Feb", "revenue": 1200},
        {"month": "Mar", "revenue": 900}
    ]
    analysis = neuronic.analyze(
        data=sales_data,
        question="What's the trend in revenue and which month performed best?"
    )

### 3. Data Generation

Generate test data with specific requirements:

    test_data = neuronic.generate(
        spec="Create realistic user profiles with name, age, occupation, and favorite color",
        n=3
    )

### 4. Context-Aware Transformation

Generate documentation with specific context:

    code_snippet = "print('hello world')"
    documentation = neuronic.transform(
        data=code_snippet,
        instruction="Generate detailed documentation for this code",
        output_type="json",
        context={
            "language": "Python",
            "audience": "beginners",
            "include_examples": True
        }
    )

### 5. Boolean Decision Making

Make simple yes/no decisions:

    sentiment = neuronic.transform(
        data="This product exceeded my expectations! Highly recommended!",
        instruction="Is this review positive?",
        output_type="bool"
    )

### 6. Python Data Structures

Generate complex Python data structures:

    data_structure = neuronic.transform(
        data="Create a nested data structure representing a family tree",
        instruction="Generate a Python dictionary with at least 3 generations",
        output_type="python"
    )

## Use Cases

### Data Processing
- Format conversion (CSV ↔ JSON ↔ XML)
- Data cleaning and normalization
- Schema transformation

### Content Generation
- Test data creation
- Sample content generation
- Documentation automation

### Analysis
- Data summarization
- Trend analysis
- Pattern recognition
- Sentiment analysis

### Development Support
- Code documentation
- API response transformation
- Test data generation
- Data validation

## API Reference

### Neuronic Class

Initialize the Neuronic class:

    neuronic = Neuronic(api_key: str = None, model: str = "gpt-3.5-turbo")

### Methods

#### transform()

Transform data according to instructions:

    result = neuronic.transform(
        data: Any,                    # Input data
        instruction: str,             # What to do with the data
        output_type: str = "string",  # Desired output format
        example: str = None,          # Optional example
        context: dict = None          # Optional context
    )

#### analyze()

Analyze data and get insights:

    result = neuronic.analyze(
        data: Any,        # Data to analyze
        question: str     # Question about the data
    )

#### generate()

Generate new data based on specifications:

    result = neuronic.generate(
        spec: str,    # What to generate
        n: int = 1    # Number of items
    )

## Best Practices

1. **API Key Security**
   - Use environment variables for API keys
   - Never commit `.env` files to version control

2. **Performance**
   - Cache frequently used transformations
   - Batch similar operations when possible

3. **Error Handling**
   - Always handle potential exceptions
   - Validate output types match expected formats

## License

MIT License - feel free to use in your own projects!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.