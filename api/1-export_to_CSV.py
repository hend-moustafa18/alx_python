import csv
import requests
from sys import argv

id = argv[1]
url1 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
empurl = f'https://jsonplaceholder.typicode.com/users/{id}'

res1 = requests.get(url1)
data1 = res1.json()

res2 = requests.get(empurl)
employeedata = res2.json()

USER_ID = employeedata['id']
USERNAME = employeedata['username']

# Extracting tasks from JSON response
tasks = [
    {
        "USER_ID": USER_ID,
        "USERNAME": USERNAME,
        "TASK_COMPLETED_STATUS": task['completed'],
        "TASK_TITLE": task['title']
    }
    for task in data1
]

# Writing to CSV file using DictWriter
csv_filename = f'{USER_ID}.csv'
with open(csv_filename, 'w', newline='') as file:
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Writing header
    writer.writeheader()

    # Writing rows
    writer.writerows(tasks)

print(f"Data has been exported to {csv_filename}")
