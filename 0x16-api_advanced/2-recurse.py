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

    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = response.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
