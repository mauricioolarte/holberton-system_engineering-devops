#!/usr/bin/python3
""" this module make a request to https://jsonplaceholder.typicode.com/users'
    and print todo list
"""

import json
import requests
import sys

if __name__ == "__main__":
    employees = requests.get('http://jsonplaceholder.typicode.com/users')
    req = requests.get('http://jsonplaceholder.typicode.com/todos')
    list = []
    resp = {}
    for employ in employees.json():
        resp[employ.get('id')] = []
    for item in req.json():
        # print(item)

        name_employe = ''

        for employ in employees.json():
            if employ.get('id') == item.get('userId'):
                username_employe = employ.get('username')

        task = {}
        task['username'] = username_employe
        task['completed'] = str(item.get('completed'))
        task['task'] = item.get('title')

        resp[item.get('userId')].append(task)

    with open('USER_ID.json', 'w') as file:
        json.dump(resp, file)
