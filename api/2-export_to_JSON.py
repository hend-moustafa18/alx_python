#!/usr/bin/python3
'''
    Retrieve user information (ID and username) using the given employee_id.
    
    Args:
        employee_id (int): The ID of the employee.
        
    Returns:
        Tuple[int, str]: A tuple containing the user's ID and username.
'''
import json
import requests
import sys

def get_user_info(employee_id):
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if user_response.status_code == 200:
        user_data = user_response.json()
        return user_data['id'], user_data['username']
    else:
        return None, None

def export_to_json(employee_id, username, todo_data):
    json_data = {str(employee_id): [{"task": task['title'], "completed": task['completed'], "username": username} for task in todo_data]}
    json_filename = f"{employee_id}.json"

    with open(json_filename, "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=2)

    print(f"Data has been exported to {json_filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_id, username = get_user_info(employee_id)

    if user_id is None:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)

    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks = response.json()

    export_to_json(employee_id, username, tasks)

if __name__ == "__main__":
    main()

