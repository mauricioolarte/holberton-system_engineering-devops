#!/usr/bin/python3
""" this module make a request to https://jsonplaceholder.typicode.com/users'
    and print todo list
"""

import requests
import csv
import sys

if __name__ == "__main__":
    name_employe = ''
    employees = requests.get('http://jsonplaceholder.typicode.com/users')
    for employ in employees.json():
        if employ.get('id') == int(sys.argv[1]):
            name_employe = employ.get('username')
    uri_to_req = ('http://jsonplaceholder.typicode.com/todos?userId=' +
                  str(sys.argv[1]))
    req = requests.get(uri_to_req)
    with open('USER_ID.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in req.json():
            USER_ID = str(sys.argv[1])
            USERNAME = name_employe
            TASK_COMPLETED_STATUS = str(task.get('completed'))
            TASK_TITLE = task.get('title')
            csv_row = [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
            writer.writerow(csv_row)
