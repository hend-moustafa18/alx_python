import csv
import os
import requests
import sys



def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['username']  # Changed from 'name' to 'username'

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos = response.json()

    # Create CSV file name
    csv_filename = os.path.join(os.getcwd(), f"{employee_id}.csv")  # Specify full path for the CSV file

    # Write data to CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Write each task to CSV
        for todo in todos:
            csv_writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])

    
    return csv_filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    csv_filename = get_employee_todo_progress(employee_id)
    