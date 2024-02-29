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

    return csv_filename  # Return the filename to use in the CSV checker script

def checkCSVFile(id, csv_filename):
    if os.path.exists(csv_filename):
        print("User ID and Username: OK")
        return True
    else:
        print("User ID and Username: Incorrect")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 1

    csv_filename = getData(id)
    if checkCSVFile(id, csv_filename):
        sys.exit(0)
    else:
        sys.exit(1)