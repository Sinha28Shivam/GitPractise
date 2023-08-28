import logging
from configparser import ConfigParser
from datetime import date
from random import randint

# Initialize logger
logging.basicConfig(level=logging.INFO, filename='employee_generator.log', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class Employee:
    def __init__(self, first_name, last_name, emp_id, manager_name, join_date, dob, salary, department_name):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_id = emp_id
        self.manager_name = manager_name
        self.join_date = join_date
        self.dob = dob
        self.salary = salary
        self.department_name = department_name

    @property
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

def generate_employee_data(num_employees=100):
        employees = []
        
        for i in range(1, num_employees + 1):
            first_name = f"Employee{i}"
            last_name = f"Lastname{i}"
            emp_id = i
            manager_name = f"Manager{i}"
            join_date = f"{randint(2015, 2023)}-{randint(1, 12):02d}-{randint(1, 28):02d}"
            dob = date(randint(1950, 2000), randint(1, 12), randint(1, 28))
            salary = randint(50000, 150000)
            department_name = f"Department{i}"
            
            employee = Employee(first_name, last_name, emp_id, manager_name, join_date, dob, salary, department_name)
            employees.append(employee)

        logging.info("Employee data generated successfully")
        return employees