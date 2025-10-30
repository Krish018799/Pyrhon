procedural = ["c", "fortran", "pascal"]
object_oriented = ["java", "c++", "python"]
functional = ["haskell", "scala", "lisp"]

user = input("Enter language = ")

if user in procedural:
    print(user, " is in procedural programming language")
elif user in object_oriented:
    print(user, " is in object oriented programming language")
elif user in functional:
    print(user, " is in functional programming language")
else:
    print(user, " is not in the list or paradigm is unknown.")