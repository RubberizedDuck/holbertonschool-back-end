#!/usr/bin/python3
"""
This module is designed to extract data from an API
and export to a CSV file
"""


import requests
from sys import argv
import csv


def get_data(user_id):
    """ retrieves data from an api """
    # setting variable for users and their todos with html of API
    user_list = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)

    # using requests to get information and converting to json format
    user_info = requests.get(user_list).json()
    todo_info = requests.get(user_todo).json()
    user_data = []

    # creates a csv file with user_id
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8', newline='') as f:
        # sets a variable to write to csv file with delimiters and quoting
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        # sets the data in a variable and writes it to each row in the csv
        for data in todo_info:
            listing = [user_id, user_info['name'],
                       data['completed'], data['title']]
            writer.writerow(listing)

# using the second argument after the file as the user id
if __name__ == "__main__":
    get_data(int(argv[1]))
