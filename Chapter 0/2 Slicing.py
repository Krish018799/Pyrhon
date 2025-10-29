# Slicing
a = "Harry"

sl = a[0:3] # Start from index 0 all the way till 3 (excluding 3)

sl1 = a[:4] # Here :4 means 0:4 if you don't write anything on the left side of the colon it takes 0 as default. Same on right side it takes -1 as default

sl2 = a[1:] # this is same as a[1:5]

print(a[:]) # this means a[0:-1]

# Print string with gaps
word = "amazing"

print(word[1: 6: 2]) # "mzn"