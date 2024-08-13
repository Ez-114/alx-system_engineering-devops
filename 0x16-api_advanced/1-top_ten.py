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
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Set custom headers to avoid being blocked for too many requests
    headers = {
        'User-Agent': 'my-reddit-api-request'
    }

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Try to parse the JSON response
        try:
            data = response.json()
            posts = data['data']['children']

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        except (KeyError, ValueError):
            # Print None if there was an issue parsing the JSON
            print(None)
    else:
        # Print None if the subreddit is invalid or another error occurs
        print(None)
