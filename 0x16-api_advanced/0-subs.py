#!/usr/bin/python3
"""
This is a module that supplies the `number_of_subscribers` function.
"""

import requests


def number_of_subscribers(subreddit):
    """
    This is a function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    rurl = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    user_agent = {'User-Agent': 'www.aphrotee.tech'}
    r = requests.get(rurl, headers=user_agent)
    if r.status_code == 200:
        resp = r.json()
        return (resp['data']['children'][0]['data']['subreddit_subscribers'])
    return 0
