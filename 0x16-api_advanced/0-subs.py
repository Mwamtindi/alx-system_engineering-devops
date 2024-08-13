#!/usr/bin/python3
"""
Script containing function that queries the Reddit API and returns the
number of subscribers for a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
