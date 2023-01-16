#!/usr/bin/python3

"""
This is a a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""


import requests
import sys


def gather_data(userId):
    """
    requests for data from given api link
    """
    apiUrl = 'https://jsonplaceholder.typicode.com/todos/'
    userUrl = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get(apiUrl)
    u = requests.get(userUrl)
    user_api = u.json()
    todo_api = r.json()
    n_tasks = 0
    n_tasks_true = 0
    tasks_titles = []
    employee_name = ""
    for user in user_api:
        if (user.get('id') == userId):
            employee_name = user.get('name')
    for employee in todo_api:
        if employee.get('userId') == userId:
            n_tasks += 1
            if employee.get('completed'):
                n_tasks_true += 1
                tasks_titles.append(employee.get('title'))
    print('Employee {} is done with tasks({}/{}):\n\t {}'
          .format(employee_name, n_tasks_true,
                  n_tasks, '\n\t '.join(tasks_titles)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            userId = int(sys.argv[1])
            gather_data(userId)
        except Exception:
            pass
