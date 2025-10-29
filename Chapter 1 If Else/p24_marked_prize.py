marked_prize = float(input("Enter marked prize: "))

if marked_prize <= 7000:
    discount = 0.10

elif marked_prize > 7000 and marked_prize <= 10000:
    discount = 0.15

elif marked_prize > 10000:
    discount = 0.20

nm = marked_prize - (discount * marked_prize)
print(nm)