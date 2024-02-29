import csv
import os
import requests
import sys

def getData(id):
    usersur1 = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todour1 = "{}/todos".format(usersur1)

    request1 = requests.get(usersur1)
    result = request1.json()
    userid = result['id']
    username = result['username']

    request2 = requests.get(todour1)
    tasks = request2.json()

    # Specify the full path to the CSV file using os.path.join
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, "{}.csv".format(userid))
    
    with open(filename, "w" , newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([userid, username, task['completed'], task['title']])

    return filename

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 1
    
    csv_filename = getData(id)
    print(f"CSV file created: {csv_filename}")