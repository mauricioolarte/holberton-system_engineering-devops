#!/usr/bin/python3
""" this module make a request to https://jsonplaceholder.typicode.com/users'
    and print todo list
"""

import json
import requests
import sys

if __name__ == "__main__":
    name_employe = ''
    employees = requests.get('http://jsonplaceholder.typicode.com/users')
    for employ in employees.json():
        if employ.get('id') == int(sys.argv[1]):
            username_employe = employ.get('username')
    uri_to_req = ('http://jsonplaceholder.typicode.com/todos?userId=' +
                  str(sys.argv[1]))
    req = requests.get(uri_to_req)
    list = []
    for elem in req.json():
        tasks = {}
        tasks['username'] = username_employe
        tasks['completed'] = str(elem.get('completed'))
        tasks['task'] = elem.get('title')
        list.append(tasks)
    resp = {}
    resp[str(sys.argv[1])] = list
    with open('USER_ID.json', 'w') as file:
        json.dump(resp, file)
