# -1+2-3+4-5

n = int(input("Enter limit=> "))

for i in range(1, n+1):
    if(i%2==0):
        print(" +", i, end="")
    else:
        print(" -", i, end="")