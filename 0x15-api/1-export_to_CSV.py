#!/usr/bin/python3
"""
Python script that uses REST API for a given employee ID, returns
information about his/her TODO list progress, and exports data in CSV format.
"""

import requests
import sys
import csv


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

    # Prepare data for CSV
    csv_data = []
    for task in tasks:
        csv_data.append([
            employee_id,
            employee_name,
            str(task.get('completed')),
            task.get('title')
        ])

    # Export to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)

    # Print summary
    done = sum(1 for task in tasks if task.get('completed'))
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))
    for task in tasks:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
