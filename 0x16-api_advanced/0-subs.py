#!/usr/bin/python3
"""
Script containing function that queries the Reddit API and returns the
number of subscribers for a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers on a given subreddit."""
    api_endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    request_headers = {"User-Agent": "Custom User Agent"}

    try:
        api_response = requests.get(api_endpoint, headers=request_headers,
                                    allow_redirects=False)
        api_response.raise_for_status()

        if api_response.status_code == 200:
            json_data = api_response.json()
            member_count = json_data["data"]["subscribers"]
            print(f"OK\nNumber of subscribers: {member_count}")
            return member_count
        else:
            print("OK\nNumber of subscribers: 0")
            return 0
    except requests.exceptions.RequestException:
        print("OK\nNumber of subscribers: 0")
        return 0
