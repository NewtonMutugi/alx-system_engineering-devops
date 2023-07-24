#!/usr/bin/python3

"""
    Using what you did in the task #0, extend your Python script to export
    data in the JSON format.

    Requirements:

    - Records all tasks that are owned by this employee
    - Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
      TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    - File name must be: USER_ID.json
"""

import json


if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()

    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump({user_id: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        } for task in todo]}, jsonfile)
