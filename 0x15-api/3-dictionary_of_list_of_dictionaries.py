#!/usr/bin/python3
"""
Python script that uses REST API to fetch TODO lists for all employees
and export the data in JSON format.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(base_url).json()

    all_employees_data = {
        user.get("id"): [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        } for todo in requests.get(f"{base_url}/{user.get('id')}/todos")
                                   .json()]
        for user in users
    }

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employees_data, jsonfile)
