#----------------------#
# HomeWork lessons 6/1 #
#----------------------#

city = input("Where would you like to rent an appartement? ")
price = int(input("What is your budget? "))

good = "This flat is good for you"
not_good = "This flat is not good for you"
if city == (("New York" or "San Francisco") and (int(price) <= 4000)):
    print(f"{good} {city}, {price}")
if city == "Washington":
    print(f"{not_good} {city}, {price}")
if city == "Chicago":
    print(f"{good} {city}, {price}")
if int(price) < 3000 :
    print(f"{good} {city}, {price}")
