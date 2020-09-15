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
            name_employe = employ.get('name')
    uri_to_req = ('http://jsonplaceholder.typicode.com/todos?userId=' +
                  str(sys.argv[1]))
    req = requests.get(uri_to_req)
    csv_file = csv.writer(open('USER_ID.csv', 'w'))
    for task in req.json():
        csv_row = [str(sys.argv[1]), name_employe, task.get('completed'),
                task.get('title')]
        csv_file.writerow(csv_row)
