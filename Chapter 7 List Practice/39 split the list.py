list1 = [11, 44, 500, 22, 99, 77]
even_indices = []
odd_indices = []
for i in range(len(list1)):
    if i % 2 == 0:
        even_indices.append(list1[i])
    else:
        odd_indices.append(list1[i])

print("Even indices:", even_indices)
print("Odd indices:", odd_indices)