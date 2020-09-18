#!/usr/bin/python3
""" make request to redit api """
import requests

parameters = {'limit': 100, 'count': 0}
listres = []
def recurse(subreddit, hot_list=[]):
    """ make request to subredit and return numbers of subscribers"""
    headers = {'User-Agent': 'Mauricio'}

    url = 'http://www.reddit.com/r/' + subreddit + '/hot/.json'
    r = requests.get(url, headers=headers, params=parameters)
    if r.status_code == 200:
        answer_list_10 = r.json().get('data').get('children')
        for top in range(len(answer_list_10)):
            hot_list.append((answer_list_10[top].get('data').get('title')))
        if len(answer_list_10) >= 100:
            parameters['after'] = r.json().get('data').get('after')
            # parameters['count'] += 100 
            recurse(subreddit, hot_list)
        else:
            return(hot_list)
    else:
        print('None')
