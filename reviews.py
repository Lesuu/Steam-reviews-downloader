'''Pulls reviews from Steam in the specified language'''
import steamreviews
import json

# Change the parameters (for a full list of parameters, check the original code)
request_params = dict()
request_params['language'] = 'english'

# Define the app ID of the desired game (default: Starfield)
app_id = 1716740
review_dict, query_count = steamreviews.download_reviews_for_app_id(app_id, chosen_request_params = request_params)

# Define the name of the output file
output_file = 'starfield_reviews.json'

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(review_dict, json_file, ensure_ascii=False, indent=4)

print(f"Reviews saved to {output_file}")
