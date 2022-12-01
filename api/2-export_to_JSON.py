#!/usr/bin/python3
"""
This module is designed to extract data from an API
and export to a json file
"""


import csv
import json
import requests
from sys import argv


def export_json_from_api(user_id):
    """ retrieves data from an api to export to json file """
    # setting variable for users and their todos with html of API
    user_list = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)

    # using requests to get information and converting to json format
    user_info = requests.get(user_list).json()
    todo_info = requests.get(user_todo).json()
    json_dict = {user_id: []}

    for data in todo_info:
        if data['userId'] == int(user_id):
            row = {"task": data['title'],
                   "completed": data['completed'],
                   "username": user_info['username']}
        json_dict[user_id].append(row)
    with open("{}.json".format(user_id), "w") as f:
        json.dump(json_dict, f)

# using the second argument after the file as the user id
if __name__ == "__main__":
    export_json_from_api(int(argv[1]))
