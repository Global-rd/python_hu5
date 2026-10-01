""""
My 2nd homework,
List and dictionary
"""

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }
}

#add user 4 programming language
prog_lang = input("please add 4 programming language (use comma): ")
user_info["prog_lang"] = prog_lang.split(",")
print(user_info["prog_lang"])

#Ascending alphabetical order
print(sorted(user_info["favourite_meals"]))

#The second-to-last item in the favorites list
print(user_info["favourite_meals"][-2])

#Add spaghetti to the favourite list
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])

#Extend the favourite meals list
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

#Delete the duplicated items
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

#Change the first and last item in favourite meals list
user_info["favourite_meals"][0] , user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1] , user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

#Add person to phone contacts
user_info["phone_contacts"]["Gréti_kicsi_mobil"] = ("+36707070707")
print(user_info["phone_contacts"])

# Remove Tim
user_info["phone_contacts"].pop("Tim")
print(user_info["phone_contacts"])

#Add 2 phone numbers for one new person
user_info["phone_contacts"]["Flóra"] = ["+36303030303" , "+36202020202"]
print(user_info["phone_contacts"])