#!/usr/bin/python3
""" make request to redit api """
import requests


def number_of_subscribers(subreddit):
    """ make request to subredit and return numbers of subscribers"""
    headers = {'User-Agent': 'Mauricio'}
    url = 'http://www.reddit.com/r/' + subreddit + '/about/.json'
    r = requests.get(url, headers=headers)
    answer = r.json().get('data').get('subscribers')
    if answer is None:
        return(0)
    else:
        return(answer)
