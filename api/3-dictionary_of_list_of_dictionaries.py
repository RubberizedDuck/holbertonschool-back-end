#!/usr/bin/python3
"""
This module is designed to extract data from an API
and export to a CSV file
"""


import csv
import json
import requests
from sys import argv


def export_json_from_api_all():
    """ retrieves all data from an api to export to json file """
    # setting variable for users and their todos with html of API
    user_list = 'https://jsonplaceholder.typicode.com/users/'
    user_todo = 'https://jsonplaceholder.typicode.com/todos'
    filename = 'todo_all_employees.json'

    # using requests to get information and converting to json format
    user_info = requests.get(user_list).json()
    todo_info = requests.get(user_todo).json()
    json_dict = {}

    # iterates through the users to get all users
    for users in user_info:
        user_tasks = []
        # iterates through the tasks to get all tasks done by users
        for tasks in todo_info:
            # if the user id matches task user id creates a dict of data
            if users.get("id") == tasks.get("userId"):
                row = {"username": users.get('username'),
                       "task": tasks.get('title'),
                       "completed": tasks.get('completed')}
                user_tasks.append(row)
        # creates the array of information to be dumped into json file
        json_dict[users.get("id")] = user_tasks

    with open(filename, "w") as jfile:
        json.dump(json_dict, jfile)

# using the second argument after the file as the user id
if __name__ == "__main__":
    export_json_from_api_all()
