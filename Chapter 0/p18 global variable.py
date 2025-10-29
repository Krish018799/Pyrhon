x = 'awesome'
def myfunc():
  global x # this will declare the value of x global
  x = 'fantastic'
myfunc()
print('Python is ' + x) # here x = 'fantastic'

# if i don't write global x than the value of x = 'awesome'