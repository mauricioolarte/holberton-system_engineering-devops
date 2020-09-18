#!/usr/bin/python3
""" make request to redit api """
import requests

parameters = {'limit': 100, 'before': null }
listres = []
def recurse(subreddit, hot_list=[]):
    """ make request to subredit and return numbers of subscribers"""
    headers = {'User-Agent': 'Mauricio'}

    url = 'http://www.reddit.com/r/' + subreddit + '/hot/.json'
    r = requests.get(url, headers=headers, params=parameters)
    if r.status_code == 200:
        answer_list_10 = r.json().get('data').get('children')
        print(len(answer_list_10.get('count')))
        for top in range(len(answer_list_10)):
            hot_list.append((answer_list_10[top].get('data').get('title')))
        parameters['before'] = r.json().get('after')
        recurse(subreddit, hot_list)
        return(hot_list)
    else:
        print('None')
