#!/usr/bin/python3


"""
This is a Python script to export data in the JSON format.
"""
import json
import requests
import sys


def gather_data_and_export_to_json(userId):
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
    js_filename = str(userId) + '.json'
    with open(js_filename, 'w+') as js_file:
        js_data = {}
        js_tasks = []

        for emp in todo_api:
            if emp.get('userId') == userId:
                js_tasks.append({"task": emp.get('title'),
                                 "completed": emp.get('completed'),
                                 "username": employee_name})
        js_data[str(userId)] = js_tasks
        js_dump = json.dumps(js_data)
        js_file.write(js_dump)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            userId = int(sys.argv[1])
            gather_data_and_export_to_json(userId)
        except Exception:
            pass
