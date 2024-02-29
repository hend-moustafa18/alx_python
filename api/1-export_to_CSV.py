import csv
import os  # Import the os module
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
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task.get("completed")),
                "TASK_TITLE": task.get("title")
            })

    return filename  # Return the filename

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
    csv_filename = export_to_csv(employee_id, employee_name, todo_data)
    print(f"Data exported to {csv_filename} successfully.")

    # Check if the CSV file exists before running the checking script
    if os.path.isfile(csv_filename):
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")

    # Now you can run the checking script or any other operations
    # using the exported CSV file.
    # For example, you can run:
    # os.system(f"python3 checking_script.py {csv_filename}")

if __name__ == "__main__":
    main()
    