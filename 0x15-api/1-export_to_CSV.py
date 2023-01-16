#!/usr/bin/python3

"""
This is a script that exports api data to CSV file
"""


import csv
import requests
import sys


def gather_data_and_export_2_csv(userId):
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
    for task in todo_api:
        if task.get('userId') == userId:
            n_tasks += 1
            if task.get('completed'):
                n_tasks_true += 1
                tasks_titles.append(task.get('title'))
    """print('Employee {} is done with tasks({}/{}):\n\t {}'
          .format(employee_name, n_tasks_true,
                  n_tasks, '\n\t '.join(tasks_titles)))"""
    csv_filename = str(userId) + '.csv'
    csv_file = open(csv_filename, 'w+')
    csv_writer = csv.writer(csv_file)
    for emp in todo_api:
        if emp.get('userId') == userId:
            csv_writer.writerow([str(userId),
                                employee_name,
                                str(emp.get('completed')),
                                emp.get('title')])
    csv_file.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            userId = int(sys.argv[1])
            gather_data_and_export_2_csv(userId)
        except Exception:
            pass
