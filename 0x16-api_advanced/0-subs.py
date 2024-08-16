#!/usr/bin/python3
"""
0-subs module

defines a funtion that returns the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
