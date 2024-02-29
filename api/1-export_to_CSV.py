import csv
import requests
import sys

def get_data(user_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"{user_url}/todos"

    response_user = requests.get(user_url)
    user_data = response_user.json()
    username = user_data['username']

    response_todos = requests.get(todos_url)
    tasks = response_todos.json()

    with open(f"{user_id}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        for task in tasks:
            writer.writerow([user_id, username, task['completed'], task['title']])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])
    else:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    get_data(user_id)
