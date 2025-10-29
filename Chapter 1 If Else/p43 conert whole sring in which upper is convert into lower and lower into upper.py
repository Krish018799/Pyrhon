text = "Hello World"
converted = ""

for char in text:
    if char.islower():
        converted += char.upper()
    elif char.isupper():
        converted += char.lower()
    else:
        converted += char  # Keep non-alphabetic characters as is

print(converted)  # Output: hELLO wORLD