import csv
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

    with open("{}.csv".format(userid), "w" , newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([userid, username, task['completed'], task['title']])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 1
    
    getData(id)
