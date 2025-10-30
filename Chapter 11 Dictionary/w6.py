items = {
    "maggie": 20,
    "parleg": 10,
    "crackjack": 20,
    "noodles": 32,
    "chips": 15,
    "cookies": 18
}
total = 0
for s,m in items.items():
    total+= m
print(total,"Rs")

# method 2:` total = sum(items.values())
