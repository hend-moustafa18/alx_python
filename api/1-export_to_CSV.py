import csv
import requests 
from sys import argv

id = argv[1]
url1 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
empurl= f'https://jsonplaceholder.typicode.com/users/{id}'

res1 = requests.get(url1)
data1 = res1.json()

res2 = requests.get(empurl)
employeedata = res2.json()

USER_ID = employeedata['id']
USERNAME = employeedata['username']
TASK_COMPLETED_STATUS = ''
TOTAL_NUMBER_OF_TASKS = len(data1)
TASK_TITLE = ''

with open(f'{USER_ID}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(data1)):
        TASK_COMPLETED_STATUS = data1[i]['completed']
        TASK_TITLE = data1[i]['title']
        writer.writerow([USER_ID,USERNAME,TASK_COMPLETED_STATUS,TASK_TITLE])
