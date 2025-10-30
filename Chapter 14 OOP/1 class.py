class Emp:
    # these are class attributes because they belong to the class
    language = "py"
    salary = 120000

rohit = Emp() # here rohit is an object

rohit.name = "rohit" # this is an object attribute or instance attribute

print(rohit.name, rohit.language)