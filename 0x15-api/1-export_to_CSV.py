#!/usr/bin/python3
""" this module make a request to https://jsonplaceholder.typicode.com/users'
    and print todo list
"""

import csv
import requests
import sys

if __name__ == "__main__":
    name_employe = ''
    employees = requests.get('http://jsonplaceholder.typicode.com/users')
    for employ in employees.json():
        if employ.get('id') == int(sys.argv[1]):
            username_employe = employ.get('username')
            name_employe = employ.get('name')
    uri_to_req = ('http://jsonplaceholder.typicode.com/todos?userId=' +
                  str(sys.argv[1]))
    req = requests.get(uri_to_req)
    with open('USER_ID.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in req.json():
            USER_ID = task.get('userId')
            USERNAME = username_employe
            TASK_COMPLETED_STATUS = str(task.get('completed'))
            TASK_TITLE = task.get('title')
            csv_row = [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
            writer.writerow(csv_row)

    count = 0
    for key in req.json():
        if key.get('completed') is True:
            count += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        name_employe, count, len(req.json())))
    for key in req.json():
        if key.get('completed') is True:
            print('\t {}'.format(key.get('title')))
