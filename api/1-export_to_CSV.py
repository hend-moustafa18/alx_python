import csv
import os
import requests
import sys

def get_user_tasks(user_id):
    # Make a request to the API to get user's tasks
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        tasks = response.json()
        return tasks
    else:
        print(f"Error: Unable to fetch tasks for user {user_id}")
        sys.exit(1)

def export_to_csv(user_id, tasks):
    # Create a CSV file with the specified format
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write each task as a new row
        for task in tasks:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": task['username'],
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })
    
    print(f"CSV file '{filename}' has been created successfully.")

def count_tasks_in_csv(user_id):
    # Check if the CSV file exists
    filename = f"{user_id}.csv"
    if os.path.exists(filename):
        # Open the CSV file and count the number of tasks
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            # Subtract 1 to exclude the header row
            num_tasks = len(list(reader)) - 1
            return num_tasks
    else:
        print(f"Error: CSV file '{filename}' not found.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user's tasks
    tasks = get_user_tasks(user_id)

    # Export tasks to CSV
    export_to_csv(user_id, tasks)

    # Count the number of tasks in CSV
    num_tasks = count_tasks_in_csv(user_id)
    print(f"Number of tasks in CSV: {num_tasks}")

if __name__ == "__main__":
    main()
    