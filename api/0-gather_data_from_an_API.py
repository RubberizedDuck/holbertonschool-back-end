#!/usr/bin/python3
"""
"""


import requests
import json

def get_data(user_id):
    """ retrieves data from an api """
    user_list = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_list = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
data = response_API.text
#print(response_API)
parse_json = json.loads(data)
print (parse_json)
