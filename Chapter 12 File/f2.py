f1 = open("abc", "r")
while True:
    ch = f1.read(1) # here 1 means if name is kavya so first k add then a add then v add and so on
    if not ch: # if ch is not in f1 then loop will break
        break
    print(ch)
f1.close()