your_expenses = {
    'Clothes': 1100,
    'Shoes': 1000,
    'Watch': 900,
    'Mobile Recharge': 699,
    'Petrol': 1980
}

your_wife = {
    'Mobile Recharge': 799,
    'DTH recharge': 999,
    'Clothes': 2310,
    'Makeup': 3670,
    'Shoes': 999
}

total1 = sum(your_expenses.values())
total2 = sum(your_wife.values())

print("1. Sum of your expenses is", total1, "sum of your wife expenses is", total2)

if total1 > total2:
    print("2. You spending more")
elif total2 > total1:
    print("2. Your wife's spending more")
else:
    print("2. Both spent equally")

combine = {}

for k in your_expenses:
    combine[k] = your_expenses[k]

for k in your_wife:
    if k in combine:
        combine[k] += your_wife[k]
    else:
        combine[k] = your_wife[k]

max_item = max(combine, key=combine.get)
print("3. Highest spending was on", max_item, "with", combine[max_item])