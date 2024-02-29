import csv
import os
import requests
import sys

def getData(id):
    users_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"{users_url}/todos"

    user_response = requests.get(users_url)
    user_data = user_response.json()

    tasks_response = requests.get(todos_url)
    tasks = tasks_response.json()

    csv_filename = f"{id}.csv"  # Use a dynamic filename based on USER_ID

    with open(csv_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # Use QUOTE_NONNUMERIC to force quoting
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Add header
        for task in tasks:
            writer.writerow([id, user_data['username'], task['completed'], task['title']])

    # Verify the CSV file by checking its existence and comparing the number of rows
    if os.path.exists(csv_filename):
        with open(csv_filename, 'r') as f:
            num_rows = sum(1 for _ in f)  # Use sum to count rows
            if num_rows == len(tasks) + 1:  # Add 1 for the header row
                print("Number of tasks in CSV: OK")
            else:
                print("Number of tasks in CSV: Incorrect")
    else:
        print("CSV file not found")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 1

    getData(id)
