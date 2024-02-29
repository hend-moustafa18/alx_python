#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the CSV format.
"""

import csv
import requests
from sys import argv

def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    todo_url = f"{base_url}users/{employee_id}/todos"
    user_url = f"{base_url}users/{employee_id}"

    try:
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()

        user_response = requests.get(user_url)
        user_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        return None

    return todo_response.json(), user_response.json()['username']

def export_to_csv(employee_id, username, todo_data):
    filename = f"{employee_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(task.get("completed")),
                "TASK_TITLE": task.get("title")
            })

    return filename

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        employee_id = argv[1]
        todo_data, username = fetch_employee_data(employee_id)

        if todo_data is not None:
            csv_filename = export_to_csv(employee_id, username, todo_data)
            print(f"Data exported to {csv_filename} successfully.")
