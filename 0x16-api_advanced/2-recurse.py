#!/usr/bin/python3
"""
Module that queries list containing the titles of all
hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing the titles of all hot articles"""

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers).json()

    if response.get("error") == 404:
        return None
    for post in response.get("data").get("children"):
        hot_list.append(post.get("data").get("title"))
    after = response.get("data").get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
