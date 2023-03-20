class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def employee_details(self):
        print("Employee Name:", self.emp_name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)
    
    def calculate_emp_salary(self, hours_worked):
        if hours_worked <= 50:
            return self.emp_salary
        else:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary / 50))
            return self.emp_salary + overtime_amount
# Create objects for each employee
emp1 = Employee("James", "ZU22", 50000, "ACCOUNTING")
emp2 = Employee("Natalia", "ZU19", 45000, "IT")

# Print employee details
emp1.employee_details()
emp2.employee_details()

# Calculate employee salary with overtime
print("Salary for James after 60 hours of work:", emp1.calculate_emp_salary(60))
print("Salary for Natalia after 40 hours of work:", emp2.calculate_emp_salary(40))