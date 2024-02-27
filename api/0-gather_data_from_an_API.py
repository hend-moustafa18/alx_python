import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Get TODO list for the employee
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    return employee_data, todo_data

def display_todo_progress(employee_data, todo_data):
    employee_name = employee_data.get('name')
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')

    for task in todo_data:
        if task['completed']:
            print(f'\t{task["title"]} (OK)')

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_info, todo_info = get_employee_info(employee_id)

    if not employee_info or not todo_info:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)

    display_todo_progress(employee_info, todo_info)
