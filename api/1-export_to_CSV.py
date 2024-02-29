import csv
import os
import requests
import sys

def getData(id):
    usersur1 = f"https://jsonplaceholder.typicode.com/users/{id}"
    todour1 = f"{usersur1}/todos"

    request1 = requests.get(usersur1)
    result = request1.json()
    userid = result['id']
    username = result['username']

    request2 = requests.get(todour1)
    tasks = request2.json()

    csv_filename = f"{userid}.csv"

    with open(csv_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([userid, username, task['completed'], task['title']])

    # Check if the number of tasks in CSV is equal to the number of tasks obtained from the API
    if os.path.exists(csv_filename):
        with open(csv_filename, 'r') as f:
            csv_reader = csv.reader(f)
            num_tasks_in_csv = sum(1 for _ in csv_reader)
            if num_tasks_in_csv == len(tasks):
                print("Number of tasks in CSV: OK")
            else:
                print("Number of tasks in CSV: Incorrect")
    else:
        print(f"Error: File {csv_filename} not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 1
    getData(id)
