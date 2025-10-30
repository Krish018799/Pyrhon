marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20
}

print("Name\t\t\tMark\t\t\tResult")

for s,m in marks.items():
    if m<18:
        print(s,"\t\t",m,"\t\t","fail")