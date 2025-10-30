class Emp:
    # these are class attributes because they belong to the class
    language = "py"
    salary = 120000

    # this is a method
    # we write self because we use object.method() it passes an argument so if we don't write self it shows an error
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    #   NOTE: we must use self when we write a method even if you don't gonna use it

    # to solve above problem we use staticmethod
    @staticmethod
    def greet():
        print("Good Morning")


rohit = Emp()
rohit.language = "JS"

rohit.getInfo() # is same as Emp.getInfo(rohit)