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

def getData(id):
    users_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"{users_url}/todos"

    user_response = requests.get(users_url)
    user_data = user_response.json()

    if not user_data:
        print(f"User with ID {id} not found.")
        return

    username = user_data['username']

    todos_response = requests.get(todos_url)
    tasks = todos_response.json()

    json_data = {str(id): [{"task": task['title'], "completed": task['completed'], "username": username} for task in tasks]}

    json_filename = f"{id}.json"

    with open(json_filename, "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=2)

    print(f"Data has been exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    getData(id)
