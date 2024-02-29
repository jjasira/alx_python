# import csv
# import requests
# import sys


# def get_employee_info(employee_id):
#     """Fetch the employee details from the given url by appending the employee_id and convert the data to json"""
#     employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
#     employee_response = requests.get(employee_url)
#     employee_data = employee_response.json()

#     """fetch the employee's todo by appending the todo route to the url"""
#     todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
#     todos_response = requests.get(todos_url)
#     todos_data = todos_response.json()

#     """create csv file for the empoyee"""
#     file_name = f"{employee_id}.csv"
#     with open(file_name, mode="w", newline='') as csv_file:
#         fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE' ]
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#         """Write the csv headers"""
#         writer.writeheader()

#         """Write the rows under the epecified columns"""
#         for task in todos_data:
#             writer.writerow({
#                 'USER_ID': employee_id,
#                 'USERNAME': employee_data['username'],
#                 'TASK_COMPLETED_STATUS': task['completed'],
#                 'TASK_TITLE': task['title']
#             })


# """Obtain the employees details from the command line using the sys module"""
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python script_name.py employee_id.")
#         sys.exit(1)

#     """Get the employee id from the second argument"""
#     employee_id = int(sys.argv[1])

#     """Call the function with the provided id"""
#     get_employee_info(employee_id)


import requests
import csv

def get_employee_info(employee_id):
    """Fetching employee details"""
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    """Fetching employee TODO list"""
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    """Creating CSV file"""
    csv_filename = f'{employee_id}.csv'

    """Writing data to CSV"""
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        """Writing header"""
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        """Writing tasks"""
        for task in todo_data:
            csv_writer.writerow([employee_id, employee_data['username'], task['completed'], task['title']])

    print(f"CSV file '{csv_filename}' created successfully.")

def get_all_employees():
    """Fetching all employees"""
    employees_url = 'https://jsonplaceholder.typicode.com/users'
    employees_response = requests.get(employees_url)
    employees_data = employees_response.json()

    """Looping through all employees"""
    for employee in employees_data:
        get_employee_info(employee['id'])

if __name__ == "__main__":
    get_all_employees()
