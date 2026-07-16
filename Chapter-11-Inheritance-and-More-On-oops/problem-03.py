# Create a class ‘Employeeʼ and add salary and increment properties to it. Write a method
# ‘salaryAfterIncrementʼ method with a @property decorator with a setter which changes
# the value of increment based on the salary.

class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = value - self.salary

emp = Employee(50000 , 5000)
print(emp.increment)                    #5000
emp.salaryAfterIncrement = 60000
print(emp.increment)                    #10000
print(emp.salaryAfterIncrement)         #60000