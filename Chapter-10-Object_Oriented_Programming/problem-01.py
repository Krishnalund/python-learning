# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = 'Microsoft'
    def __init__(self, name , language , salary):
        self.name = name
        self.language = language
        self.salary = salary

employee1 = Programmer('John','Python',1200000)
employee2 = Programmer('Jennie','JavaScript',1200000)
print(employee1.company, employee1.name , employee1.language, employee1.salary)
print(employee2.company, employee2.name , employee2.language, employee2.salary)

