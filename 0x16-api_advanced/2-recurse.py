#!/usr/bin/python3
"""Function to query all hot articles of a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively return a list of titles of all hot articles in a subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "ChangeMeClient/0.1 by /u/Affectionate-Cry1141"
    }
    params = {"limit": 100, "after": after}
    
    response = requests.get(
                url, 
                headers=headers, 
                params=params, 
                allow_redirects=False)
    
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    
    if not results:
        return None

    hot_list.extend([child.get("data").get("title") for child in results.get("children")])

    after = results.get("after")
    
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
