import csv
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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user's tasks
    tasks = get_user_tasks(user_id)

    # Export tasks to CSV
    export_to_csv(user_id, tasks)

if __name__ == "__main__":
    main()
