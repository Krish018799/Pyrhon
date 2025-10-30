marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20,
    "anita": 25
}

c = 0
for s,m in marks.items():
    if m>=18:
        c+=1
print("Number of passed students: ", c)