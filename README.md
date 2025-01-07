# Steam reviews downloader
 A python script using woctezuma's Steam Reviews Downloader script (https://github.com/woctezuma/download-steam-reviews) to pull reviews from Steam in a json format, as well as a Python script to format the output to be more readable.

 This code downloads reviews from one Steam game at a time and places them in a json folder. A second script allows you to clean up the produced file, keeping only a few parameters. For more options, use the original code.

## Usage
 Install steamreviews on your computer by running the following command with python: 
 ```
 pip install steamreviews
 ```
 Modify the `app_id` parameter in the `reviews.py` to the Steam App ID of your desired game (the number that appears in the game's steam page URL). Run this script to get a .json file with the downloaded data. This returns reviews with the following format:
 ```
    "184859252": {
        "recommendationid": "184859252",
        "author": {
            "steamid": "76561197992061034",
            "num_games_owned": 0,
            "num_reviews": 2,
            "playtime_forever": 4757,
            "playtime_last_two_weeks": 2755,
            "playtime_at_review": 4726,
            "last_played": 1736103794
        },
        "language": "english",
        "review": "There are parts of the writing or lack of consequences, BUT by and large, this game is fantastic fun for hours and hours of distraction.",
        "timestamp_created": 1736101935,
        "timestamp_updated": 1736101935,
        "voted_up": true,
        "votes_up": 0,
        "votes_funny": 0,
        "weighted_vote_score": 0,
        "comment_count": 0,
        "steam_purchase": true,
        "received_for_free": false,
        "written_during_early_access": false,
        "primarily_steam_deck": false
    },
 ```
 You can either use this json file as is, or you can use the `cleanup.py` script to clean it up to a more compact format:
 ```
    "184859252": {
        "author_steamid": "76561197992061034",
        "review": "There are parts of the writing or lack of consequences, BUT by and large, this game is fantastic fun for hours and hours of distraction.",
        "voted_up": true,
        "votes_up": 0,
        "timestamp_created": "2025-01-05 18:32:15"
    },
 ```
