# Product Recommendation System with Ethical AI Practices

# Sample data: Users' browsing/purchase history and product info
users_history = {
  'alice': ['laptop', 'mouse'],
  'bob': ['headphones', 'speaker'],
  'carol': ['keyboard', 'mouse'],
}

products = [
  {'id': 1, 'name': 'Wireless Mouse', 'category': 'accessories', 'brand': 'BrandA'},
  {'id': 2, 'name': 'Gaming Keyboard', 'category': 'accessories', 'brand': 'BrandB'},
  {'id': 3, 'name': 'Laptop', 'category': 'computers', 'brand': 'BrandC'},
  {'id': 4, 'name': 'Bluetooth Speaker', 'category': 'audio', 'brand': 'BrandD'},
  {'id': 5, 'name': 'Noise Cancelling Headphones', 'category': 'audio', 'brand': 'BrandE'},
]

# Track flagged recommendations for feedback
flagged_recommendations = set()

def recommend_products(user):
  # Get user's history
  history = users_history.get(user, [])
  recommendations = []
  explanations = []

  # Fairness: Do not favor brands/categories, recommend based on similarity to history
  for product in products:
    # Simple similarity: recommend products in categories or names matching history
    relevance = 0
    for item in history:
      if item.lower() in product['name'].lower() or item.lower() == product['category']:
        relevance += 1
    if relevance > 0:
      recommendations.append(product)
      # Transparency: Explain why this product is recommended
      explanations.append(
        f"Recommended '{product['name']}' because you viewed/purchased similar items: {history}."
      )

  # If no relevant products, recommend diverse options (fairness)
  if not recommendations:
    # Avoid bias: show a mix from different categories/brands
    diverse = []
    seen_categories = set()
    for product in products:
      if product['category'] not in seen_categories:
        diverse.append(product)
        seen_categories.add(product['category'])
    recommendations = diverse
    explanations = [
      f"Recommended '{p['name']}' to introduce you to new categories." for p in recommendations
    ]

  return recommendations, explanations

def flag_recommendation(user, product_id):
  # User feedback: Allow flagging irrelevant/incorrect recommendations
  flagged_recommendations.add((user, product_id))
  print(f"Recommendation for product ID {product_id} flagged by user '{user}'.")

# Example usage
if __name__ == "__main__":
  user = 'alice'
  recs, expls = recommend_products(user)
  print(f"Recommendations for {user}:")
  for product, explanation in zip(recs, expls):
    print(f"- {product['name']} (Category: {product['category']}, Brand: {product['brand']})")
    print(f"  Explanation: {explanation}")

  # Simulate user feedback
  flag_recommendation(user, recs[0]['id'])

  # Show flagged recommendations
  print("\nFlagged recommendations:")
  for flagged in flagged_recommendations:
    print(f"User: {flagged[0]}, Product ID: {flagged[1]}")

# Inline comments throughout the code explain how each part supports ethical AI:
# - Fairness: Recommendations are based on user history, not brand/category favoritism.
# - Transparency: Each recommendation includes an explanation.
# - User feedback: Users can flag recommendations, supporting continuous improvement.
# - Explainable logic: No black-box models; recommendations are based on simple, interpretable rules.