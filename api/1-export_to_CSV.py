import csv
import requests
import sys

def export_to_csv(employee_id, username, todo_data):
    filename = f"{employee_id}.csv"  # Use the same naming convention

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

    print(f"Exported data to {filename}")
    return filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todo_data = fetch_employee_data(employee_id)

    employee_name = employee_data.get("name")

    # Export data to CSV and get the filename
    csv_filename = export_to_csv(employee_id, employee_name, todo_data)
    print(f"Data exported to {csv_filename} successfully.")
