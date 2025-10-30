class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    # when you use property decorator, you can access method like an attribute means you can return any value from method without calling it
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45

e.name = "Shahrukh Khan"
print(e.fname, e.lname)

e.show()