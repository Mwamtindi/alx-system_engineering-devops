#!/usr/bin/python3
"""Module containing function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit."""


def top_ten(subreddit):
    """Queries Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests
    api_response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                                .format(subreddit),
                                headers={"User-Agent": "My-Custom-User-Agent"},
                                allow_redirects=False)
    if api_response.status_code >= 300:
        print('None')
    else:
        [print(post.get("data").get("title"))
            for post in api_response.json().get("data").get("children")]
