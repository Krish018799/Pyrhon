country = {
    'china':143,
    'india':136,
    'usa':32,
    'uk':21
}

print("option1 = print")
print("option2 = add")
print("option3 = remove")
print("option4 = query")

option = int(input("Enter option=> "))

if option == 1:
    for k,v in country.items():
        print(k,"==>",v)

elif option == 2:
    new_country = input("Enter country: ")
    if new_country in country:
        print("Country already exists")
    else:
        population = int(input("Enter population: "))
        country[new_country] = population
        print("Country added")
        print(new_country,"==>",population)

elif option == 3:
    new_country = input("Enter country: ")
    if new_country in country:
        del country[new_country]
        print("Country removed")
    else:
        print("Country not found")

elif option == 4:
    new_country = input("Enter country: ")
    if new_country in country:
        print("Population: ", country[new_country])
    else:
        print("Country not found")

else:
    print("Wrong option!")