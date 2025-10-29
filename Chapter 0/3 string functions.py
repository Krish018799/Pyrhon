str = 'harry'

# to print the length of the string we use len() function
print(len(str)) # output: 5

"hello".upper()  # Output: 'HELLO'

"HELLO".lower()  # Output: 'hello'

"hello world".title()  # Output: 'Hello World' # capitalize first letter of each word

"python".capitalize()  # Output: 'Python'

"Hello".swapcase()  # Output: 'hELLO' converts lower into uppercase and vice versa

# Returns the first index of substring or -1 if not found.
"hello".find("e")  # Output: 1

# Returns the last index of substring.
"hello hello".rfind("hello")  # Output: 6

# Similar to find() but raises an error if not found.
"hello".index("e")  # Output: 1

# Counts occurrences of a substring.
"banana".count("a")  # Output: 3

# Checks if string starts with given prefix.
"python".startswith("py")  # Output: True

# Checks if string ends with given suffix.
"python".endswith("on")  # Output: True

# Checks if all characters are letters.
"abc".isalpha()  # Output: True

# Checks if all characters are digits.
"123".isdigit()  # Output: True

# Checks if string has only letters and numbers.
"abc123".isalnum()  # Output: True

# Checks if string contains only whitespace.
"   ".isspace()  # Output: True

# Check case format.
"hello".islower()  # Output: True
"hello".isupper()  # Output: False
print("hello".istitle())  # Output: False

# Replace occurrences of a substring.
"hello world".replace("world", "Python")  # Output: 'hello Python'

# Remove whitespace (or specific chars) from both/left/right.
"  hello  ".strip()  # Output: 'hello'

# Splits string into a list by separator.
"a,b,c".split(",")  # Output: ['a', 'b', 'c']

'''
rsplit(sep)
Similar to split() but from the right.
'''

# Splits string into lines.
"a\nb\nc".splitlines()  # Output: ['a', 'b', 'c']

# Joins elements of an iterable into a string.
",".join(["a", "b", "c"])  # Output: 'a,b,c'

# Used for string formatting.
"Hello, {}".format("John")  # Output: 'Hello, John'

# f-strings (Python 3.6+)
name = "John"
f"Hello, {name}"  # Output: 'Hello, John'

# zfill(width)
# Pads string with zeros on the left.
"7".zfill(3)  # Output: '007'