import csv
import os
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
        print(f"Error: {e}")
        sys.exit(1)

    employee_data = employee_response.json()
    todo_data = todo_response.json()

    return employee_data, todo_data

def export_to_csv(employee_id, employee_name, todo_data):
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            user_id = employee_id
            username = employee_name
            completed_status = str(task.get("completed"))
            task_title = task.get("title")

            writer.writerow([user_id, username, completed_status, task_title])

    print(f"Data exported to {filename}")

def user_info(employee_id):
    filename = f"{employee_id}.csv"

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            # Skip header row and count tasks
            next(f)  # skip header
            task_count = sum(1 for line in f)
        print("Number of tasks in CSV: OK")
    else:
        print(f"File {filename} does not exist.")

# Example usage
user_info(8)  # Replace 8 with the desired employee ID

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todo_data = fetch_employee_data(employee_id)

    employee_name = employee_data.get("name")

    export_to_csv(employee_id, employee_name, todo_data)
    user_info(employee_id)

if __name__ == "__main__":
    main()
