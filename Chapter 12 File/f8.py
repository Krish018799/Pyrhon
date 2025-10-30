f1 = open("abc", "r")

while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        pass
    else:
        print(ch, end="")
f1.close()
