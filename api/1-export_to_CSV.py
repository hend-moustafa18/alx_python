import csv
import requests
import sys

def getData(id):
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todos_url = "{}/todos".format(users_url)

    user_response = requests.get(users_url)
    user_data = user_response.json()

    if not user_data:
        print(f"User with ID {id} not found.")
        return

    username = user_data['username']

    todos_response = requests.get(todos_url)
    tasks = todos_response.json()

    csv_filename = "{}.csv".format(id)  # Use a dynamic filename

    with open(csv_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Add header
        for task in tasks:
            writer.writerow([id, username, task['completed'], task['title']])

    print(f"Data has been exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    getData(id)
