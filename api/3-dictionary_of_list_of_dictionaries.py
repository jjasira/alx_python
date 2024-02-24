"""Export data from JSONPlaceholder API to JSON format."""

import json
import requests
from sys import argv

"""Prevent the module from running when imported"""
if __name__ == '__main__':
    user_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    
    """Fetching user data"""
    user_data = requests.get(user_url).json()
    username = user_data.get('username')

    """ Fetching tasks data"""
    tasks_data = requests.get(url).json()

    """ Creating a dictionary to store tasks for the user"""
    user_tasks = {user_id: []}

    """ Populating the dictionary with tasks data"""
    for task in tasks_data:
        task_data = {
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        }
        user_tasks[user_id].append(task_data)

    """Creating or updating the todo_all_employees.json file"""
    try:
        with open('todo_all_employees.json', 'r') as file:
            all_tasks = json.load(file)
    except FileNotFoundError:
        all_tasks = {}

    all_tasks.update(user_tasks)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)

    print(f'Tasks for user {user_id} exported to todo_all_employees.json')