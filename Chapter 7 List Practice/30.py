india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Q.1
user1 = input("Enter city name = ")

if user1 in india:
    print(user1, " is belongs to India")
elif user1 in pakistan:
    print(user1, " is belongs to Pakistan")
elif user1 in bangladesh:
    print(user1, " is belongs to Bangladesh")

# Q.2
user2 = input("Enter two city1 => ")
user3 = input("Enter two city2 => ")

if user2 in india and user3 in india:
    print("Both cities are in india")
elif user2 in pakistan and user3 in pakistan:
    print("Both cities are in pakistan")
elif user2 in bangladesh and user3 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")