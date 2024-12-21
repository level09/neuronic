from neuronic import Neuronic
import json
from typing import List, Dict

# Initialize with OpenAI's flagship model
neuronic = Neuronic(model="gpt-4o")

# Example 1: Recipe Transformer using the new decorator
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

# Example 2: Story Generator with Context
@neuronic.function(output_type="string")
def generate_mini_story(character: str, setting: str, mood: str) -> str:
    """Create a three-sentence story based on the given character, setting, and mood."""
    pass

story = generate_mini_story(
    character="a curious robot",
    setting="ancient library",
    mood="mysterious"
)
print("\nGenerated Story:", story)

# Example 3: Smart Data Cleaning
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
print("\nCleaned Data:", json.dumps(clean_data, indent=2))

# Example 4: Code Style Converter
python_code = """
def calculate_stats(numbers):
    total = 0
    for n in numbers:
        total += n
    avg = total / len(numbers)
    return {'sum': total, 'average': avg}
"""

@neuronic.function(output_type="string")
def convert_to_functional_style(code: str) -> str:
    """Convert imperative Python code to a more functional programming style using list comprehensions, map, filter, etc."""
    pass

functional_code = convert_to_functional_style(python_code)
print("\nFunctional Style Code:", functional_code)

# Example 5: Smart Text Analysis
movie_review = """
Inception (2010) blew my mind! The visuals were stunning and the plot kept me guessing.
While some found it confusing, I thought the complexity added to its charm.
The ending still has people debating to this day. 🎬 Must watch! Rating: 9/10
"""

analysis = neuronic.analyze(
    data=movie_review,
    question="What aspects of the movie did the reviewer focus on and what's their overall sentiment?"
)
print("\nReview Analysis:")
print(f"Answer: {analysis['answer']}")
print(f"Confidence: {analysis['confidence']}")
print(f"Reasoning: {analysis['reasoning']}")

# Example 6: Creative Data Generation
emoji_personas = neuronic.generate(
    spec="""Create unique emoji-based character profiles with:
    - Emoji combination for appearance
    - Personality trait
    - Favorite hobby
    - Life motto""",
    n=3
)
print("\nEmoji Personas:", json.dumps(emoji_personas, indent=2))

# Example 7: Smart Format Conversion
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
print("\nTask Board:", json.dumps(task_board, indent=2))

# Example 8: Smart Data Enrichment
basic_product = {
    "name": "Vintage Leather Backpack",
    "price": 79.99,
    "category": "bags"
}

@neuronic.function(output_type="json")
def enrich_product_data(product: Dict) -> Dict:
    """
    Enhance product data with:
    - SEO-friendly description
    - Target audience
    - Suggested keywords
    - Related products
    - Seasonal relevance
    """
    pass

enriched_product = enrich_product_data(basic_product)
print("\nEnriched Product Data:", json.dumps(enriched_product, indent=2)) 