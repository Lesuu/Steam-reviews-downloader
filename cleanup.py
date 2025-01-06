"""Cleans up the 'starfield_reviews.json' corpus assembled using the 'reviews.py' file."""
import json
from datetime import datetime

with open('starfield_reviews.json', 'r', encoding='utf-8') as file:
    reviews_data = json.load(file)

reviews = reviews_data.get("reviews", {})

review_count = len(reviews)

cleaned_reviews = dict()

for review_id, review in reviews.items():
    cleaned_review = {
        "author_steamid": review['author']['steamid'],
        "review": review['review'],
        "voted_up": review['voted_up'],
        "timestamp_created": datetime.utcfromtimestamp(review['timestamp_created']).strftime('%Y-%m-%d %H:%M:%S')
    }

    # If timestamp_updated is different from timestamp_created"
    if review['timestamp_created'] != review['timestamp_updated']:
        cleaned_review["timestamp_updated"] = datetime.utcfromtimestamp(review['timestamp_updated']).strftime('%Y-%m-%d %H:%M:%S')

    cleaned_reviews[review_id] = cleaned_review

cleaned_data = {"reviews": cleaned_reviews}

with open('cleaned_starfield_reviews.json', 'w', encoding='utf-8') as cleaned_file:
    json.dump(cleaned_data, cleaned_file, ensure_ascii=False, indent=4)


print(f"{review_count} cleaned reviews saved to 'cleaned_starfield_reviews.json'")
