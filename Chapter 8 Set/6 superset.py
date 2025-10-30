set1={11,22,33,44,55,66}
set2={11,33,55}
set3={1,2,3,4,9,11,55,66}
set4={8,9,7}

print(set1.issuperset(set2)) # it prints true if set2 members are in set1 and prints false if set2 members are not in set1
print(set1.issuperset(set3))
print(set1.issuperset(set4))