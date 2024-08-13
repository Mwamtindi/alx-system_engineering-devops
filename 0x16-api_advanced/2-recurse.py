#!/usr/bin/python3
"""
Module with function that queries the Reddit API and returns list of
titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Fxn recursively fetch all hot post titles from a subreddit."""
    api_endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    request_headers = {"User-Agent": "Custom User Agent"}
    query_params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    api_response = requests.get(api_endpoint, headers=request_headers,
                                params=query_params, allow_redirects=False)
    if api_response.status_code == 200:
        response_data = api_response.json().get("data")
        next_page = response_data.get("after")
        count += response_data.get("dist")
        for post in response_data.get("children"):
            hot_list.append(post.get("data").get("title"))
        if next_page is not None:
            return recurse(subreddit, hot_list, next_page, count)
        else:
            return hot_list
    else:
        return None
