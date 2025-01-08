"""Cleans up the corpus assembled using the 'reviews.py' file."""
import json
from datetime import datetime

# File input and output names
INPUT_FILE = 'reviews.json'
OUTPUT_FILE = 'cleaned_reviews.json'

with open(INPUT_FILE, 'r', encoding='utf-8') as file:
    reviews_data = json.load(file)

reviews = reviews_data.get("reviews", {})

review_count = len(reviews)

cleaned_reviews = list()

for review_id, review in reviews.items():
    cleaned_review = {
        "review_id": review_id,
        "author_steamid": review['author']['steamid'],
        "review": review['review'],
        "voted_up": review['voted_up'],
        "votes_up": review['votes_up'],
        "votes_funny": review['votes_funny'],
        # Converts the unix time used in the steam database to readable time
        "timestamp_created": datetime.utcfromtimestamp(review['timestamp_created']).strftime('%Y-%m-%d %H:%M:%S')
    }

    # If timestamp_updated is different from timestamp_created"
    if review['timestamp_created'] != review['timestamp_updated']:
        cleaned_review["timestamp_updated"] = datetime.utcfromtimestamp(review['timestamp_updated']).strftime('%Y-%m-%d %H:%M:%S')

    cleaned_reviews.append(cleaned_review)

cleaned_data = {"reviews": cleaned_reviews}

with open(OUTPUT_FILE, 'w', encoding='utf-8') as cleaned_file:
    json.dump(cleaned_data, cleaned_file, ensure_ascii=False, indent=4)


print(f"{review_count} cleaned reviews saved to {OUTPUT_FILE}")
