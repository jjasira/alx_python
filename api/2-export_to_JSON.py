"""Import the needed modules in alphabetical order"""
import json
import requests
import sys

"""This function will take an employee's id as an argument and return a json file with the required details"""
def get_employee_info(employee_id):
    """Fetch the employee details from the given url by appending the employee_id and convert the data to json"""
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    """fetch the employee's todo by appending the todo route to the url"""
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    """create a json file for the employee with required format"""
    json_file_path = f"{employee_id}.json"
    json_data = {
        f"{employee_id}": [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_data['username']
            }
            for task in todos_data
        ]
    }

    """Write the json file with the required details"""
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
"""Obtain the employees details from the command line using the sys module"""
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id.")
        sys.exit(1)

    """Get the employee id from the second argument"""
    employee_id = int(sys.argv[1])

    """Call the function with the provided id"""
    get_employee_info(employee_id)