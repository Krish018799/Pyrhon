class Employee:
    company = "ITC"
    salary = 120000

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

# this is how you can inherit parent or base class to child or inherited or derived class
class Programmer(Employee):
    company = "ITC Infotech"
    language = "Python"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee("Raju")
b = Programmer("Sanjay")

print(a.company, b.company)
b.show()