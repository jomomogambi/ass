class Employee():
    def _init__(self, id,name):
        self.id=id
        self.name=name
class SalaryEmployee(Employee):
    def _init__(self, salary):
        self.salary=salary
    def calculate_payroll(self):
        return super().calculate_payroll()
class HourlyEmployee(Employee):
    def _init__(self, salary, hours_worked, rate):
        self.salary=salary
        self.hours_worked=hours_worked
        self.rate=rate
        self.hours_worked * self.rate
class CommissionEmployee(SalaryEmployee):
    def _init__(self, salary, commission_rate, sales):
        self.commission_rate=commission_rate
        self.sales=sales
    def calculate_payroll(self):
        fixed_salary=super().calculate_payroll()
        commission=self.commission_rate * self.sales
        return fixed_salary + commission
class PayrollCalculator():
    def _init__(self, calculate_payroll):
        self.calculate_payroll=calculate_payroll
        def SalaryEmployee(self):
            SalaryEmployee=self.calculate_payroll
            HourlyEmployee=(2 * 0.15) + self.calculate_payroll
            CommissionEmployee=(0.34 * 10000) + calculate_payroll
cp=PayrollCalculator(20000)
cp.SalaryEmployee()
cp.HourlyEmployee
cp.CommissionEmployee()
print("Payroll for", cp.SalaryEmployee, ":", cp.calculate_payroll())
print("Payroll for", cp.HourlyEmployee, ":", cp.calculate_payroll())
print("Payroll for", cp.CommissionEmployee, ":", cp.calculate_payroll())