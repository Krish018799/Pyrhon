students={1:"Ram", 22:"Jayul", 3:"Rahul",44:"Anjali",50:"Riya"}
print(students)

students[33]="Hiral"
print(students)

students.setdefault(101,"Sita")
print(students)

students.setdefault(102,"") # If the key already exists, it does nothing and returns the current value. If the key does not exist, it adds the key with the given default_value, and returns that value.
students[102]="Ravan"

print(students)
