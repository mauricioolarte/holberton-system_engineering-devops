#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    name_employe = ''
    employees = requests.get('https://jsonplaceholder.typicode.com/users')
    for employ in employees.json():
        if employ.get('id') == int(sys.argv[1]):
            name_employe = employ.get('name')
    uri_to_req = ('https://jsonplaceholder.typicode.com/todos?userId=' +
                  str(sys.argv[1]))
    req = requests.get(uri_to_req)
    count = 0
    for key in req.json():
        if key.get('completed') is True:
            count += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        name_employe, count, len(req.json())))
    for key in req.json():
        if key.get('completed') is True:
            print('\t {}'.format(key.get('title')))
