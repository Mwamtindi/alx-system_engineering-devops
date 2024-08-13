#!/usr/bin/python3
"""
Script containing function that queries the Reddit API and returns the
number of subscribers for a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers on a given subreddit."""
    api_endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request_headers = {"User-Agent": "Mozilla/5.0"}
    api_response = requests.get(api_endpoint, headers=request_headers,
                                allow_redirects=False)
    if api_response.status_code == 200:
        json_data = api_response.json()
        member_count = json_data['data']['subscribers']
        return member_count
    else:
        return 0
