#!/usr/bin/python3
"""Module containing recursive function that queries Reddit API, parses
the title of all hot articles, and prints a sorted count of given keywords"""
import requests


def fetch_hot_posts(forum):
    """Fxn Fetch hot posts from the Reddit API"""
    api_endpoint = f"https://www.reddit.com/r/{forum}/hot.json"
    request_headers = {"User-Agent": "Reddit Keyword Counter"}
    api_response = requests.get(api_endpoint, headers=request_headers)
    response_data = api_response.json()
    return response_data.get("data", {}).get("children", [])


def count_words(subreddit, word_list, word_index=0, word_counts=None):
    """
    Recursively queries Reddit API and prints a sorted count of given
    case-insensitive keywords from hot posts for a given subreddit
    """
    if word_counts is None:
        word_counts = {}
    if word_index < len(word_list):
        current_word = word_list[word_index].lower()
        hot_posts = fetch_hot_posts(subreddit)
        for post in hot_posts:
            post_title = post["data"]["title"].lower()
            word_counts[current_word] = word_counts.get(current_word, 0)
            + post_title.count(current_word)
        count_words(subreddit, word_list, word_index + 1, word_counts)
    else:
        sorted_word_counts = sorted(word_counts.items(), key=lambda x:
                                    (-x[1], x[0]))
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java'".format(sys.argv[0]))
    else:
        target_subreddit = sys.argv[1]
        keyword_list = sys.argv[2:]
        count_words(target_subreddit, keyword_list)
