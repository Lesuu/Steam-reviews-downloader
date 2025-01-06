import steamreviews
import json

# Change the parameters
request_params = dict()
request_params['language'] = 'english'

# Define the app ID of Starfield 
app_id = 1716740
review_dict, query_count = steamreviews.download_reviews_for_app_id(app_id, chosen_request_params = request_params)

print(f"{query_count} reviews found")

with open('starfield_reviews.json', 'w', encoding='utf-8') as json_file:
    json.dump(review_dict, json_file, ensure_ascii=False, indent=4)

print("Reviews saved to 'starfield_reviews.json'")