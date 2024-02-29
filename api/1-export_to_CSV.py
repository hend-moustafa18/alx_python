import csv
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

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for task in todo_data:
            writer.writerow([
                employee_id,
                employee_name,
                str(task.get("completed")),
                task.get("title")
            ])

    print(f"Data exported to {filename} successfully.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todo_data = fetch_employee_data(employee_id)

    employee_name = employee_data.get("name")

    # Export data to CSV
    export_to_csv(employee_id, employee_name, todo_data)

if __name__ == "__main__":
    main()
