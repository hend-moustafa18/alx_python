"""
This module contains an api that exports to JSON
"""
import json
import requests


def export_all_tasks_to_json():
    # Dictionary to store tasks for all employees
    all_tasks = {}

    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Iterate over each user to fetch their tasks
    for user in users_data:
        user_id = user['id']
        username = user['username']

        # Fetch tasks for the user
        todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # Add tasks to the dictionary
        all_tasks[user_id] = [{"username": username, "task": todo['title'], "completed": todo['completed']} for todo in todos]

    # Create JSON file name
    json_filename = "todo_all_employees.json"

    # Write data to JSON file
    with open(json_filename, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)

   

if __name__ == "__main__":
    export_all_tasks_to_json()