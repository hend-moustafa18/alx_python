import csv
import requests
from sys import argv

def export_tasks_to_csv(user_id, username, tasks):
    filename = f"{user_id}.csv"
    try:
       with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([user_id, username, task["completed"], task["title"]])
        print(f"CSV file {filename} created successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to export tasks to CSV
export_tasks_to_csv(user_id, username, tasks)
