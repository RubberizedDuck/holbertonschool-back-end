#!/usr/bin/python3
"""
This module is designed to extract data from an API
"""


import requests
from sys import argv


def get_data(user_id):
    """ retrieves data from an api """
    # setting variable for users and their todos with html of API
    user_list = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_list = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)

    # using requests to get information and converting to json format
    user_info = requests.get(user_list).json()
    todo_info = requests.get(todo_list).json()
    total_tasks = len(todo_info)
    completed_tasks = 0

    # incrementing over the todo's to get how many tasks completed by user
    for item in todo_info:
        if item['completed']:
            completed_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(user_info['name'],
                                                         completed_tasks,
                                                         total_tasks))

    # incrementing over completed tasks
    # to print out tasks that have been completed
    for item in todo_info:
        if item['completed']:
            print('\t {}'.format(item['title']))


# using the second argument after the file as the user id
if __name__ == "__main__":
    get_data(int(argv[1]))
