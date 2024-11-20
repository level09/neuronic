from neuronic import Neuronic

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