#!/usr/bin/python3

"""
    Using what you did in the task #0, extend your Python script to export
    data in the JSON format.

    Requirements:

    - Records all tasks from all employees
    - Format must be: { "USER_ID": [ {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID"
    : [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    - File name must be: todo_all_employees.json
"""

import json


if __name__ == "__main__":
    import requests
    import sys

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump({user.get('id'): [{
            "username": user.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in todo if user.get('id') == task.get('userId')]
            for user in users}, jsonfile)
