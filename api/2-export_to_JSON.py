#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""
import json

def export_tasks_to_json(user_id, username, tasks):
    data = {user_id: []}
    for task in tasks:
        data[user_id].append({"task": task["title"], "completed": task["completed"], "username": username})

    filename = f"{user_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Example data
user_id = "123"
username = "example_user"
tasks = [
    {"title": "Task 1", "completed": True},
    {"title": "Task 2", "completed": False},
    {"title": "Task 3", "completed": True}
]

export_tasks_to_json(user_id, username, tasks)
