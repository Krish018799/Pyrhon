desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']

# Q.1
print("Total deserts in the list = ", len(desserts))

# Q.2
desserts.insert(0, 'macaron')
print(desserts)

# Q.3
desserts.remove('pavlova')
ice_cream = desserts.index("ice cream")
desserts.insert(ice_cream+1, "pavlova")
print(desserts)