import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    # Define the URL to query the Reddit API for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

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
            return data['data']['subscribers']
        except (KeyError, ValueError):
            # Return 0 if there was an issue parsing the JSON
            return 0
    else:
        # For other error codes, assume invalid subreddit
        return 0
