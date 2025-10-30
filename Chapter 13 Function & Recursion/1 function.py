# Function: we use def function_name(): to define function

# basic function
# this is function definition
def name():
    print("hello")

name()

# FUNCTIONS WITH ARGUMENTS
def sum(num1, num2):
    ans = num1 + num2
    return ans

print(sum(2,3)) # here sum() is known as function call

# default parameter
def mul(num1 = 3, num2 = 6):
    result = num1 * num2
    return result

print(mul()) # we didn't pass any parameter so it takes default value
print(mul(2, 3))