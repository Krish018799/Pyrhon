dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]

for x in dice_result:
    if x == 6:
        c = dice_result.count(x)

print("you got 6s ", c, " times")


# method 2

# use print(dice_result.count(6))