#!/usr/bin/python3

"""
0-gather_data_from_as_API

This script retrieves a given employee's to-do list information from
the JSONPlaceholder API and prints the number of completed tasks along
with their titles.

Usage:
    python3 0-gather_data_from_as_API <employee_id>

Args:
    employee_id (int): The ID of the employee whose
                    to-do list information is to be retrieved.
"""

import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":

    # Get employee id from command-line
    emp_id = sys.argv[1] if len(sys.argv) >= 2 else exit()

    # Format URLs
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

    # Request employee name
    with urlopen(emp_url) as response:
        emp_name = json.loads(response.read()).get('name')

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
