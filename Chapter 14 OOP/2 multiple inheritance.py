class Employee:
    company = "ITC"
    salary = 120000

    def show(self):
        print(f"The name is {self.company} and salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

# Multiple inheritance
class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguage()