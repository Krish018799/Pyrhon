list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2]

first_max = max(list1)
second_max= float('-inf')
for y in list1:
    if y != first_max and y>second_max:
            second_max = y

print("The second max value is = ", second_max)