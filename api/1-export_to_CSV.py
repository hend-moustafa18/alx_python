import csv
import requests
import sys

def getData(id):
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todos_url = "{}/todos".format(users_url)

    user_response = requests.get(users_url)
    user_data = user_response.json()

    tasks_response = requests.get(todos_url)
    tasks = tasks_response.json()

    csv_filename = "8.csv"  # Use a fixed filename

    with open(csv_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Add header
        for task in tasks:
            writer.writerow([id, user_data['username'], task['completed'], task['title']])

    # Check if the number of tasks in CSV is equal to the number of tasks obtained from the API
    with open(csv_filename, 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Skip the header
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
