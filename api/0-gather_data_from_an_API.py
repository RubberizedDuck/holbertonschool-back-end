#!/usr/bin/python3
"""
"""


import requests
import json
response_API = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response_API.text
#print(response_API)
parse_json = json.loads(data)
print (parse_json)
