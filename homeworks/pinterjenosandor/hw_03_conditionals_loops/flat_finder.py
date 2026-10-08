'''
this line wher we input the city name where Shara want to rent a flat,
modify the inputed data, cut the spaces from the begin, and the end from the text
the inputed city name also modified, because if the first letter of every part will be
capitalized, even if it was written in lower case
'''
city = input("Add a city where do you want to rent: ").strip().title()
'''
price input clould be a float type, now convert the string to integer
'''
price = int(input("Add a price: "))
currency = ("$") # need for the f-string result

rent_places = {
    "liked" : ["New York","San Francisco"],
    "favourite" : ["Chicago"],
    "hate" : ["Washington"]
} 
#print(type(rent_places["liked"]))
#print(city)
if price <= 0: # if the input is not correct, add a text back for the user, to give a correct number
    print("Please try again with correct price, the value not to be negative and zero")
else:
    if city in rent_places["liked"]: # can rent if the city is in the liked list and under 4000
        rentable = price < 4000
    elif city in rent_places["favourite"]: #can rent, because thi is the most favourite place, money no problem
        rentable = True
    elif city in rent_places["hate"]: # can't rant, because this city is in the hate list
        rentable = False
    elif city == "Szolnok": #that is my Easter Egg :)
        print("You found the city where I born!")
        rentable = True
    else: # can rant if the price is equal or lower than 3000
        rentable = price <= 3000 
yes_or_not = "can" if rentable else "cannot" #rentable or not for result text
the_case_of_washington = "Because she hate this city!" if city in rent_places["hate"] else "" # extra why not Washington
#result
print(f"Sarah {yes_or_not} rent a flat in {city} for {price}{currency}/month. {the_case_of_washington}")