#!/usr/bin/python3
import requests
import sys

def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{base_url}users/{employee_id}"
    todo_url = f"{base_url}users/{employee_id}/todos"

    try:
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg = f"Error: {e}"
        print(f"{error_msg[:26]:<26}")
        sys.exit(1)

    employee_data = employee_response.json()
    todo_data = todo_response.json()

    return employee_data, todo_data

def display_todo_progress(employee_name, completed_tasks, total_tasks, task_data):
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in task_data:
        print(f"\t{task['title'][:50]:<50}")

def main():
    if len(sys.argv) != 2:
        usage_msg = "Usage: python3 script_name.py <employee_id>"
        print(f"{usage_msg[:26]:<26}")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        error_msg = "Employee ID must be an integer."
        print(f"{error_msg[:26]:<26}")
        sys.exit(1)

    employee_data, todo_data = fetch_employee_data(employee_id)

    employee_name = employee_data.get("name")
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    display_todo_progress(employee_name, completed_tasks, total_tasks, todo_data)

if __name__ == "__main__":
    main()
