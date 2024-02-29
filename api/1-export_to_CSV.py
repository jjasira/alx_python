import csv
import requests


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
