# Neuronic 🧠

<p align="center">
  <img src="https://raw.githubusercontent.com/level09/neuronic/main/.github/images/neuronic.png" alt="Neuronic Logo" width="440"/>
</p>

Imagine Python functions that can think, reason, and create - functions that understand natural language, analyze complex data patterns, and generate creative solutions. Welcome to Neuronic - where we transform ordinary Python code into intelligent, AI-powered modules that bring GPT's cognitive capabilities directly into your codebase, complete with enterprise-grade validation, caching, and error handling.


<p align="center">
  <img src="https://raw.githubusercontent.com/level09/neuronic/main/.github/images/neuronic-features.png" alt="Neuronic chart" width="440"/>
</p>

## ✨ Magic in Three Lines

```python
from neuronic import Neuronic

@neuronic.function(output_type="json")
def convert_to_vegetarian(recipe: str) -> dict:
    """Convert any food recipe to its vegetarian version while maintaining the flavor profile."""
    pass

# That's it! Your function is now AI-powered 🌱
veggie_recipe = convert_to_vegetarian("Classic Beef Burger with bacon")
```

## 🌟 Real-Time Streaming

Watch your AI functions generate responses in real-time:

```python
@neuronic.function(output_type="string", stream=True)
def write_story(prompt: str) -> str:
    """Write a creative story based on the given prompt."""
    pass

# See the story being written in real-time
for chunk in write_story("A curious robot discovers an ancient library"):
    print(chunk, end="")

# Or use the transform method directly
neuronic = Neuronic()
for chunk in neuronic.transform(
    data="Explain quantum computing",
    instruction="Write a clear, step-by-step explanation",
    stream=True
):
    print(chunk, end="")
```

## 🌟 What is Neuronic?

Neuronic is your gateway to building intelligent Python applications powered by GPT-4o. Create functions that can understand context, extract insights, and solve complex problems - all while maintaining the reliability and predictability of traditional programming. With built-in validation, type checking, and caching, Neuronic makes AI as dependable as any other Python module.

## 🚀 Features

- **🎯 Smart Function Decorator:** Transform any Python function into an AI-powered one with a simple decorator
- **🧠 Real-Time Streaming:** Watch AI responses generate in real-time with built-in streaming support
- **🧠 Intelligent Understanding:** Create functions that truly understand your data, extracting meaning and insights
- **🗣️ Natural Language Processing:** Process text like a human - analyze sentiment, extract key information, and understand context
- **✍️ Creative Generation:** Generate human-quality content, from documentation to test data, tailored to your specifications
- **🔍 Pattern Recognition:** Uncover hidden patterns and relationships in your data through GPT-powered analysis
- **📦 Multiple Output Types:** Get results in any format you need - strings, numbers, JSON, lists, booleans, or Python structures
- **🏢 Enterprise Ready:** Built-in validation, type checking, and caching ensure production-ready outputs
- **⚡ Performance Optimized:** Automatic chunking for large inputs and smart caching for repeated operations

## 🛠️ Quick Start

### Installation

```bash
pip install neuronic
```

### Configuration

```python
# Option 1: Use environment variables (.env file)
OPENAI_API_KEY=your-openai-api-key-here

# Option 2: Pass API key directly
neuronic = Neuronic(api_key="your-api-key-here")
```

## 🎮 Cool Examples

### 🪄 Smart Function Decorator
Transform any Python function into an AI-powered one:

```python
@neuronic.function(output_type="string")
def generate_mini_story(character: str, setting: str, mood: str) -> str:
    """Create a three-sentence story based on the given character, setting, and mood."""
    pass

story = generate_mini_story(
    character="a curious robot",
    setting="ancient library",
    mood="mysterious"
)
```

### 🧹 Smart Data Cleaning
Clean and standardize messy data:

```python
@neuronic.function(output_type="json")
def clean_user_data(users: List[Dict]) -> List[Dict]:
    """
    Clean and standardize user data:
    - Properly capitalize names
    - Validate and fix email addresses
    - Convert age to numbers
    """
    pass

clean_data = clean_user_data(messy_data)
```

### 🎨 Creative Generation
Generate emoji-based character profiles:

```python
emoji_personas = neuronic.generate(
    spec="""Create unique emoji-based character profiles with:
    - Emoji combination for appearance
    - Personality trait
    - Favorite hobby
    - Life motto""",
    n=3
)
```

### 📊 Smart Analysis
Analyze text with context and reasoning:

```python
analysis = neuronic.analyze(
    data=movie_review,
    question="What aspects of the movie did the reviewer focus on?"
)
print(f"Answer: {analysis['answer']}")
print(f"Confidence: {analysis['confidence']}")
print(f"Reasoning: {analysis['reasoning']}")
```

## 🎯 Perfect For

- **🔄 Data Processing:** Format conversion, cleaning, normalization
- **📝 Content Creation:** Documentation, test data, sample content
- **📊 Analysis:** Pattern recognition, sentiment analysis, trend detection
- **🛠️ Development:** Code transformation, API handling, validation

## 🧰 API Reference

### Core Methods

```python
# Transform data with streaming
result = neuronic.transform(
    data=input_data,               # What to transform
    instruction="your instruction", # How to transform it
    output_type="string",          # What format you want
    stream=True,                   # Enable streaming
    example=None,                  # Optional example
    context=None                   # Optional context
)
for chunk in result:
    print(chunk, end="")

# Analyze data
insights = neuronic.analyze(
    data=your_data,      # What to analyze
    question="your question"  # What to find out
)

# Generate data
new_data = neuronic.generate(
    spec="what to generate",  # What you want
    n=1                      # How many items
)
```

### Streaming Functions

```python
# Create streaming functions for long-form content
@neuronic.function(output_type="string", stream=True)
def write_blog_post(topic: str, style: str) -> str:
    """Write a detailed blog post in the specified style."""
    pass

# Watch the blog post being written in real-time
for chunk in write_blog_post(
    topic="The Future of AI",
    style="conversational"
):
    print(chunk, end="")

# Stream JSON responses
@neuronic.function(output_type="json", stream=True)
def analyze_text_stream(text: str) -> dict:
    """Analyze text and return structured data with streaming."""
    pass

# Note: JSON streaming ensures valid JSON output
for chunk in analyze_text_stream("Your text here"):
    print(chunk, end="")
```

## 🎓 Best Practices

1. **🔐 Security First**
   - Keep API keys in environment variables
   - Never commit sensitive data

2. **⚡ Performance Tips**
   - Use caching for repeated operations
   - Enable streaming for long-running operations
   - Batch similar requests when possible
   - Be mindful of token limits when streaming

3. **🛡️ Error Handling**
   - Always handle exceptions gracefully
   - Validate outputs match expected formats
   - Handle streaming interruptions properly

4. **🔄 Streaming Guidelines**
   - Use streaming for long-form content generation
   - Handle partial outputs appropriately
   - Consider disabling streaming for small, quick operations
   - Remember streaming bypasses caching

## 📜 License

MIT License - feel free to use in your own projects!

## 🤝 Contributing

Got ideas? Found a bug? Contributions are welcome! Feel free to:
- Open an issue
- Submit a pull request
- Share your cool use cases

## 🌟 Star Us!
If you find Neuronic useful, give us a star! It helps others discover the project.