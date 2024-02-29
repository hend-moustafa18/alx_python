import csv
import requests
import sys

def getData(id):
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todos_url = "{}/todos".format(users_url)

    response_user = requests.get(users_url)
    user_data = response_user.json()
    username = user_data['username']

    response_todos = requests.get(todos_url)
    todos = response_todos.json()

    filename = "{}.csv".format(id)
    
    with open(filename, "w" , newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([id, username, task['completed'], task['title']])

    return filename

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 1
    
    csv_filename = getData(id)
    print(f"CSV file created: {csv_filename}")
