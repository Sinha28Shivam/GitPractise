import pandas as pd
from employee_generator import generate_employee_data

def display_employees():
    employees = generate_employee_data()
    df = pd.DataFrame(employees)

    print("Employee Data:")
    print(df)

if __name__ == "__main__":
    display_employees()