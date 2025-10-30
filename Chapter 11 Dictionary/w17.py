month = {
    'january':2200,
    'fabruary':2350,
    'march':2600,
    'april':2130,
    'may':2190,
    'june':1980,
    'july':2400,
    'august':2250,
    'september':2100,
    'octomber':2400,
    'november':2150,
    'december':2500
}

# 1
diff = month['fabruary'] - month['january']
print("1.",diff," dollars are spend extra compared to January")

# 2
total = month['january'] + month['fabruary'] + month['march']
print("2.",total)

# 3
if 2400 in month.values():
    print("3. Yes,you spent exactly 2400 dollars in any month.")
else:
    print("3. No,you spent exactly 2400 dollars in any month.")

# 4
month['june'] = 2080
print("4. The new value of june expence is", month['june'])

# 5
month['april'] -=200
print("5. The new expance in april after refund is ", month['april'])

# 6
high_month = max(month, key=month.get)
print("6. Highest expense:", high_month, "=", month[high_month])

# 7
total = month["January"] + month["February"] + month["March"] + month["April"] + month["May"] + month["June"]
print("7. Avg of Jan to June:", total / 6)

# 8
low_month = min(month, key=month.get)
print("8. Lowest expense:", low_month, "=", month[low_month])