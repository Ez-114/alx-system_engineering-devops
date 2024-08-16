#!/usr/bin/python3
"""
1-top_ten module

defines a function that prints the titles of the first 10 hot posts for
a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    # Define the URL to query the Reddit API for hot posts
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Set custom headers to avoid being blocked for too many requests
    headers = {
        'User-Agent': 'ChangeMeClient/0.1 by /u/Affectionate-Cry1141'
    }

    # Make a GET request to the Reddit API
    response = requests.get(
                url, 
                headers=headers,
                params={"limit": 10})

    # Check if the request was successful
    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        # Print None if the subreddit is invalid or another error occurs
        print(None)
