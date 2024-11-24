from neuronic import Neuronic
import json

# Initialize
neuronic = Neuronic()

# Example 1: Data Transformation
customer_data = "John Doe, john@example.com, New York"
contact_card = neuronic.transform(
    data=customer_data,
    instruction="Convert this CSV data into a contact card format",
    output_type="json",
    example='{"name": "Jane Doe", "email": "jane@example.com", "location": "Los Angeles"}'
)
print("Contact Card:", contact_card)

# Example 2: Data Analysis
sales_data = [
    {"month": "Jan", "revenue": 1000},
    {"month": "Feb", "revenue": 1200},
    {"month": "Mar", "revenue": 900}
]
analysis = neuronic.analyze(
    data=sales_data,
    question="What's the trend in revenue and which month performed best?"
)
print("Analysis:", analysis)

# Example 3: Data Generation
test_data = neuronic.generate(
    spec="Create realistic user profiles with name, age, occupation, and favorite color",
    n=3
)
print("Generated Profiles:", test_data)

# Example 4: Complex Transformation with Context
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
print("Documentation:", documentation)

# Example 5: Boolean Decision Making
sentiment = neuronic.transform(
    data="This product exceeded my expectations! Highly recommended!",
    instruction="Is this review positive?",
    output_type="bool"
)
print("Is Positive:", sentiment)

# Example 6: Generate Python Data Structures
data_structure = neuronic.transform(
    data="Create a nested data structure representing a family tree",
    instruction="Generate a Python dictionary with at least 3 generations",
    output_type="python"
)
print("Family Tree:", data_structure)

# Example 7: Large Context Processing
long_text = """
# Introduction to Machine Learning

Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.

## Supervised Learning

Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs. It infers a function from labeled training data consisting of a set of training examples.

### Common Algorithms
1. Linear Regression
2. Logistic Regression
3. Decision Trees
4. Random Forests
5. Support Vector Machines (SVM)
6. Neural Networks

## Unsupervised Learning

Unsupervised learning is a type of machine learning algorithm used to draw inferences from datasets consisting of input data without labeled responses.

### Common Algorithms
1. K-means clustering
2. Hierarchical clustering
3. Principal Component Analysis (PCA)
4. Independent Component Analysis (ICA)

## Reinforcement Learning

Reinforcement learning is an area of machine learning concerned with how intelligent agents ought to take actions in an environment in order to maximize the notion of cumulative reward.

### Key Concepts
1. Agent
2. Environment
3. State
4. Action
5. Reward

## Deep Learning

Deep learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning.

### Popular Architectures
1. Convolutional Neural Networks (CNN)
2. Recurrent Neural Networks (RNN)
3. Long Short-Term Memory (LSTM)
4. Transformers

## Applications

Machine learning has numerous real-world applications:
- Image and Speech Recognition
- Natural Language Processing
- Recommendation Systems
- Autonomous Vehicles
- Medical Diagnosis
- Financial Trading
- Fraud Detection

## Challenges

Common challenges in machine learning:
1. Data Quality and Quantity
2. Overfitting and Underfitting
3. Feature Selection
4. Model Selection
5. Computational Resources
6. Interpretability
7. Ethical Considerations

## Future Directions

The field of machine learning continues to evolve with:
- Automated Machine Learning (AutoML)
- Few-shot Learning
- Meta Learning
- Quantum Machine Learning
- Edge Computing
"""

# Process the long text with multiple questions
summary = neuronic.transform(
    data=long_text,
    instruction="Create a concise summary of this machine learning text, highlighting the main topics and key points",
    output_type="string"
)
print("\nSummary:", summary)

# Extract structured information
topics = neuronic.transform(
    data=long_text,
    instruction="Extract all main topics and their key algorithms/concepts into a structured format",
    output_type="json",
    example='''
    {
        "topics": [
            {
                "name": "Supervised Learning",
                "algorithms": ["Linear Regression", "Logistic Regression"]
            }
        ]
    }
    '''
)
print("\nStructured Topics:", json.dumps(topics, indent=2))

# Generate study questions
questions = neuronic.transform(
    data=long_text,
    instruction="Generate 5 comprehensive study questions based on this content",
    output_type="list"
)
print("\nStudy Questions:", json.dumps(questions, indent=2))

# Example 8: Large Dataset Analysis
large_sales_data = [
    {"month": "Jan", "revenue": 1000, "products": ["A", "B", "C"], "region": "North"},
    {"month": "Feb", "revenue": 1200, "products": ["B", "C", "D"], "region": "North"},
    {"month": "Mar", "revenue": 900, "products": ["A", "C", "E"], "region": "South"},
    # ... (repeated 100 times with variations to make it large)
] * 100  # This makes the dataset large enough to trigger chunking

# Analyze the large dataset
analysis_result = neuronic.analyze(
    data=large_sales_data,
    question="What are the main trends in revenue across regions and what products are most frequently sold?"
)
print("\nLarge Dataset Analysis:")
print("Answer:", analysis_result["answer"])
print("Confidence:", analysis_result["confidence"])
print("Reasoning:", analysis_result["reasoning"])

# Another example with the previous long ML text
ml_analysis = neuronic.analyze(
    data=long_text,  # Using the long_text from previous example
    question="What are the key differences between supervised, unsupervised, and reinforcement learning according to the text?"
)
print("\nML Text Analysis:")
print("Answer:", ml_analysis["answer"])
print("Confidence:", ml_analysis["confidence"])
print("Reasoning:", ml_analysis["reasoning"]) 