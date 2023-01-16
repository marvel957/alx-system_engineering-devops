#!/usr/bin/python3

"""
This is a Python script to export data in the JSON format.
"""
import json
import requests


def gather_all_data_and_export_to_json():
    """
    requests for data from given api link
    """
    apiUrl = 'https://jsonplaceholder.typicode.com/todos/'
    userUrl = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get(apiUrl)
    u = requests.get(userUrl)
    user_api = u.json()
    todo_api = r.json()
    js_data = {}
    employee_name = ""
    for user in user_api:
        userId = user.get('id')
        employee_name = user.get('name')
        js_tasks = []
        for emp in todo_api:
            if emp.get('userId') == userId:
                js_tasks.append({"task": emp.get('title'),
                                 "completed": emp.get('completed'),
                                 "username": employee_name})
        js_data[str(userId)] = js_tasks

    js_filename = 'todo_all_employees.json'
    with open(js_filename, 'w+') as js_file:
        js_dump = json.dumps(js_data)
        js_file.write(js_dump)


if __name__ == '__main__':
    try:
        gather_all_data_and_export_to_json()
    except Exception:
        pass
