import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "employees.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")
employees = pd.read_csv(file_path)

print(employees.columns)

print("Data preview:\n", employees.head())

max_salary = employees['Salary'].max()
min_salary = employees['Salary'].min()
print(f"Max Salary: {max_salary}")
print(f"Min Salary: {min_salary}")

department_summary = employees.groupby('Department').agg(
    Total_Salary=('Salary', 'sum'),
    Employee_Count=('Name', 'count') 
).reset_index()

print("\nDepartment Summary:\n", department_summary)
high_salary_employees = employees[employees['Salary'] == max_salary]
high_salary_employees.to_csv("high_salary_employee.csv", index=False)

department_summary.to_csv("department_summary.csv", index=False)

print("\nFiles saved: high_salary_employee.csv, department_summary.csv")

plt.figure(figsize=(10,5))
plt.bar(department_summary['Department'], department_summary['Total_Salary'])
plt.title('Total Salary Expenses by Department')
plt.xlabel('Department')
plt.ylabel('Total Salary')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
plt.bar(department_summary['Department'], department_summary['Employee_Count'], color='orange')
plt.title('Number of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.show()