class Emp:
    language = "py"
    salary = 120000

    # Constructor which is automatically called
    # this method will execute as soon as the object is created
    # it is also known as Dunder method(Method which starts from double underscore)
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("i am creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


rohit = Emp("rohit", "JS", 1200000)
rohit.language = "JS"
rohit.name = "rohan"

print(rohit.name, rohit.language, rohit.salary)

# rohan = Emp() # this will show an error bcz we don't pass any arguments