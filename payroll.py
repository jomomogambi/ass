class Employee:
    def _init_(self, id, name):
        self.id = id
        self.name = name
        
class PayrollCalculator:
    def calculate_payroll(self):
        pass
        
class SalaryEmployee(Employee, PayrollCalculator):
    def _init_(self, id, name, salary):
        super()._init_(id, name)
        self.salary = salary
        
    def calculate_payroll(self):
        return self.salary
        
class HourlyEmployee(Employee, PayrollCalculator):
    def _init_(self, id, name, hours_worked, hourly_rate):
        super()._init_(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
        
class CommissionEmployee(SalaryEmployee):
    def _init_(self, id, name, salary, commission_rate, sales):
        super()._init_(id, name, salary)
        self.commission_rate = commission_rate
        self.sales = sales
        
    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        commission = self.sales * self.commission_rate
        return fixed_salary + commission

# create instances of the classes
salary_employee = SalaryEmployee(1, "John", 5000)
hourly_employee = HourlyEmployee(2, "Jane", 40, 20)
commission_employee = CommissionEmployee(3, "Bob", 4000, 0.1, 5000)

# calculate payroll for each employee
print("Payroll for", salary_employee.name, ":", salary_employee.calculate_payroll())
print("Payroll for", hourly_employee.name, ":", hourly_employee.calculate_payroll())
print("Payroll for", commission_employee.name, ":", commission_employee.calculate_payroll())