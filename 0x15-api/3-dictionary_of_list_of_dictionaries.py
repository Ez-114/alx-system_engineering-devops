#!/usr/bin/python3

"""
0-gather_data_from_as_API

This script retrieves a given employee's to-do list information from
the JSONPlaceholder API and prints the number of completed tasks along
with their titles.
"""

import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":

    # Format URLs
    todo_url = f"https://jsonplaceholder.typicode.com/todos/"
    emp_url = f"https://jsonplaceholder.typicode.com/users/"

    # Request employee name
    with urlopen(emp_url) as response:
        emps = json.loads(response.read())

    # Request employee todos
    with urlopen(todo_url) as response:
        todos = json.loads(response.read())

    emp_dict = {}

    for emp in emps:
        emp_id = str(emp.get('id'))
        emp_username = emp.get('username')

        tasks = []
        for todo in todos:
            if todo.get('userId') == int(emp_id):
                task_info = {
                    "username": emp_username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                }
                tasks.append(task_info)

        emp_dict.update({emp_id: tasks})

    # Write data to a custom JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(emp_dict, json_file)
