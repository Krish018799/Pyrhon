class Emp:
    # these are class attributes because they belong to the class
    language = "py"
    salary = 120000

rohit = Emp()
rohit.language = "JS" # instance attribute # Note: Instance attributes, take preference over class attributes during assignment & retrieval.
rohit.name = "rohit" # this is an object attribute or instance attribute

print(rohit.name, rohit.language, rohit.salary)