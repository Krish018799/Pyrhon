class Employee:
    a = 1

    # class method
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45

e.show() # bcz of class method it shows 1
print(e.a) # this will show 45 not 1 but if you make another object it will show 1

d = Employee()

print(d.a) # this will show 1