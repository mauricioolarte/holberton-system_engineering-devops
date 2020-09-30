#!/usr/bin/python3
""" make request to redit api """
import requests


def number_of_subscribers(subreddit):
    """ make request to subredit and return numbers of subscribers"""
    headers = {'User-Agent': 'Mauricio'}
    url = 'http://www.reddit.com/r/' + subreddit + '/about/.json'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        answer = r.json().get('data').get('subscribers')
        return(answer)
    else:
        return(0)
