from neuronic import Neuronic
import json
from typing import List, Dict
import time

# Initialize with OpenAI's flagship model
neuronic = Neuronic(model="gpt-4o")

print("🌟 Example 1: Recipe Transformer")
@neuronic.function(output_type="json")
def convert_to_vegetarian(recipe: str) -> Dict:
    """Convert any food recipe to its vegetarian version while maintaining the flavor profile."""
    pass

meat_recipe = """
Classic Beef Burger:
- 500g ground beef
- 2 burger buns
- 1 onion
- 2 slices cheese
- lettuce and tomato
- salt and pepper
"""

veggie_version = convert_to_vegetarian(meat_recipe)
print("Vegetarian Recipe:", json.dumps(veggie_version, indent=2))

print("\n🌟 Example 2: Streaming Story Generator")
@neuronic.function(output_type="string", stream=True)
def write_story(prompt: str, style: str) -> str:
    """Write a creative story in the specified style."""
    pass

print("Generating story in real-time...")
for chunk in write_story(
    prompt="A time traveler visits ancient Egypt",
    style="mysterious and suspenseful"
):
    print(chunk, end="")
    time.sleep(0.01)  # Optional: Slow down output for better readability

print("\n\n🌟 Example 3: Streaming Technical Documentation")
@neuronic.function(output_type="string", stream=True)
def write_documentation(topic: str, format: str) -> str:
    """Generate detailed technical documentation."""
    pass

print("Generating documentation in real-time...")
for chunk in write_documentation(
    topic="GraphQL API Authentication",
    format="markdown"
):
    print(chunk, end="")
    time.sleep(0.01)

print("\n\n🌟 Example 4: Smart Data Cleaning")
messy_data = [
    {"name": "jOHn DOE  ", "email": "JOHN@example.com", "age": "twenty five"},
    {"name": "Jane smith", "email": "jane@example", "age": "28"},
    {"name": "  Bob Wilson", "email": "bob@test.com", "age": "thirty"},
]

@neuronic.function(output_type="json")
def clean_user_data(users: List[Dict]) -> List[Dict]:
    """
    Clean and standardize user data:
    - Properly capitalize names
    - Validate and fix email addresses
    - Convert age to numbers
    - Remove extra whitespace
    """
    pass

clean_data = clean_user_data(messy_data)
print("Cleaned Data:", json.dumps(clean_data, indent=2))

print("\n🌟 Example 5: Streaming Code Generation")
@neuronic.function(output_type="string", stream=True)
def generate_code(spec: str, language: str) -> str:
    """Generate code based on specification."""
    pass

print("Generating Python code in real-time...")
for chunk in generate_code(
    spec="Create a FastAPI endpoint that handles user registration with email verification",
    language="python"
):
    print(chunk, end="")
    time.sleep(0.01)

print("\n\n🌟 Example 6: Smart Text Analysis")
movie_review = """
Inception (2010) blew my mind! The visuals were stunning and the plot kept me guessing.
While some found it confusing, I thought the complexity added to its charm.
The ending still has people debating to this day. 🎬 Must watch! Rating: 9/10
"""

analysis = neuronic.analyze(
    data=movie_review,
    question="What aspects of the movie did the reviewer focus on and what's their overall sentiment?"
)
print("Review Analysis:")
print(f"Answer: {analysis['answer']}")
print(f"Confidence: {analysis['confidence']}")
print(f"Reasoning: {analysis['reasoning']}")

print("\n🌟 Example 7: Streaming JSON Generation")
@neuronic.function(output_type="json", stream=True)
def analyze_text_stream(text: str) -> Dict:
    """Analyze text and return structured data with streaming."""
    pass

print("Analyzing text with streaming JSON output...")
for chunk in analyze_text_stream(movie_review):
    print(chunk, end="")
    time.sleep(0.01)

print("\n\n🌟 Example 8: Creative Data Generation")
emoji_personas = neuronic.generate(
    spec="""Create unique emoji-based character profiles with:
    - Emoji combination for appearance
    - Personality trait
    - Favorite hobby
    - Life motto""",
    n=3
)
print("Emoji Personas:", json.dumps(emoji_personas, indent=2))

print("\n🌟 Example 9: Direct Streaming Transform")
print("Generating explanation with streaming...")
for chunk in neuronic.transform(
    data="Explain how quantum computers work",
    instruction="Write a clear, beginner-friendly explanation",
    stream=True
):
    print(chunk, end="")
    time.sleep(0.01)

# Example 10: Smart Format Conversion
print("\n\n🌟 Example 10: Format Conversion")
markdown_notes = """
# Meeting Notes - Project Phoenix
## Attendees
- Alice (Team Lead)
- Bob (Developer)
- Charlie (Designer)

## Action Items
1. Update UI mockups
2. Fix login bug
3. Plan next sprint

## Next Meeting
Thursday, 2pm PST
"""

@neuronic.function(output_type="json")
def convert_to_task_board(notes: str) -> Dict:
    """Convert meeting notes into a structured task board format with status tracking."""
    pass

task_board = convert_to_task_board(markdown_notes)
print("Task Board:", json.dumps(task_board, indent=2)) 