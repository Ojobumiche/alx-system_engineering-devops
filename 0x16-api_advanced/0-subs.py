#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """ Set a custom User-Agent in headers to prevent API errors"""
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    """ Construct the API URL for the given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    """ Make a GET request to the API"""
    response = requests.get(url, headers=headers)

    """ Check if the response is successful"""
    if response.status_code == 200:
        try:
            data = response.json()
            """ Extract the number of subscribers from the response"""
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0
