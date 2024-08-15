#!/usr/bin/python3
"""0-gather_data_from_as_API

This script makes a HTTP GET request to jsonplaceholder
to recive a given employee's todo-list info
"""

import json
import sys
from urllib.request import urlopen


# Get employee id from command-line
emp_id = sys.argv[1] if len(sys.argv) >= 2 else exit()

# Format URLs
todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

# Request employee name
with urlopen(emp_url) as response:
    emp_name = json.loads(response.read())['name']


# Request employee todos
with urlopen(todo_url) as response:
    todos = json.loads(response.read())


# Completed todo titles
todo_titles = []
total_completed = 0
total_todos = 0
for todo in todos:
    total_todos += 1

    if todo['completed'] is True:
        total_completed += 1
        todo_titles.append(todo['title'])

# Print formatted text
print("Employee {} is done with \
tasks({}/{}):".format(emp_name, total_completed, total_todos))

for title in todo_titles:
    print("\t {}".format(title))
