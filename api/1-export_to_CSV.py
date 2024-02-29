import csv
import os  # Import the os module
import requests
import sys

def create_empty_csv(user_id):
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

def getData(id):
    create_empty_csv(id)  # Call create_empty_csv to create an empty CSV file if it doesn't exist

    users_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"{users_url}/todos"

    user_response = requests.get(users_url)
    user_data = user_response.json()

    tasks_response = requests.get(todos_url)
    tasks = tasks_response.json()

    csv_filename = f"{id}.csv"

    with open(csv_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([id, user_data['username'], task['completed'], task['title']])

    with open(csv_filename, 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        num_tasks_in_csv = sum(1 for _ in csv_reader)

    if num_tasks_in_csv == len(tasks):
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 1

    getData(id)
