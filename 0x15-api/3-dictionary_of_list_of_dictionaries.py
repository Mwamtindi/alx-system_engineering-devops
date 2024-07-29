#!/usr/bin/python3
"""
Python script that uses REST API to fetch TODO lists for all employees
and export the data in JSON format.
"""

import requests
import json


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"

    # Fetch all users
    response = requests.get(base_url)
    users = response.json()

    # Prepare data for JSON
    all_employees_data = {}

    for user in users:
        employee_id = str(user['id'])
        username = user['username']

        # Fetch todos for this user
        todo_url = f"{base_url}/{employee_id}/todos"
        response = requests.get(todo_url)
        tasks = response.json()

        # Prepare user's tasks
        user_tasks = []
        for task in tasks:
            user_tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

        # Add user's tasks to the main dictionary
        all_employees_data[employee_id] = user_tasks

    # Export to JSON
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(all_employees_data, json_file)

    print(f"Data exported to {filename}")
