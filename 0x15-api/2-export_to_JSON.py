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
        emp_username = json.loads(response.read()).get('username')

    # Request employee todos
    with urlopen(todo_url) as response:
        todos = json.loads(response.read())

    # Task preparation
    tasks = []
    for todo in todos:
        task_info = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": emp_username
        }
        tasks.append(task_info)

    emp_tasks = {emp_id: tasks}

    # Write data to a custom JSON file
    json_filename = f"{emp_id}.json"
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(emp_tasks, json_file)
