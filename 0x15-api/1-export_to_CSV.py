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

import csv
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

    # Prepare data for CSV
    csv_data = []
    for todo in todos:
        csv_data.append([
            emp_id,
            emp_name,
            todo.get('completed'),
            todo.get('title')
        ])

    # Write data to CSV file
    csv_filename = f"{emp_id}.csv"
    with open(csv_filename, mode='w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(csv_data)
