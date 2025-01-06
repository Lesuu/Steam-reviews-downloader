import steam_reviews
import json

# Fetch reviews for the specified app
app_id = '1716740'  # Sarfield App ID
reviews = steam_reviews.get(app_id, printProgress = True)

# Save the reviews to a JSON file
output_file = "starfield_reviews.json"

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(reviews, f, indent=4, ensure_ascii=False)

print(f"Saved {len(reviews)} reviews to {output_file}")
