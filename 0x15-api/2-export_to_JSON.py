#!/usr/bin/python3
"""
Python script that uses REST API for a given employee ID, returns
information about his/her TODO list progress, and exports data in JSON format.
"""

import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    employee = response.json()
    employee_name = employee.get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    # Prepare data for JSON
    json_data = {employee_id: []}
    for task in tasks:
        json_data[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    # Export to JSON
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)

    # Print summary
    done = sum(1 for task in tasks if task.get('completed'))
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))
    for task in tasks:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
