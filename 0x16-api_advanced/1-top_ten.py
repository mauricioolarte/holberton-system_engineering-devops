#!/usr/bin/python3
""" make request to redit api """
import requests


def top_ten(subreddit):
    """ make request to subredit and return numbers of subscribers"""
    headers = {'User-Agent': 'Mauricio'}
    parameters = {'limit': 10}
    url = 'http://www.reddit.com/r/' + subreddit + '/hot/.json'
    r = requests.get(url, headers=headers, params=parameters)
    if r.status_code == 200:
        answer_list_10 = r.json().get('data').get('children')
        for top in range(len(answer_list_10)):
            print(answer_list_10[top].get('data').get('title'))
    else:
        print('None')
