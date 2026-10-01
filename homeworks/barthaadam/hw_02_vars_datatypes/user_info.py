from pprint import pprint
# This is a dictionary that contains information about a user.

user_info = {
    "name" : "Mike",
    "age" : 25,
    "favourite_meals" : [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts" : {
        "Mary" : "+36701234567",
        "Tim" : "+36207654321",
        "Tim2" : "+36304567321",
        "Jim" : "+364005000"
    }

}

# 1. Ask the user for 4 programming languages

programming_languages = input(
    "Enter 4 programming languages separated by commas: "
)
skills = programming_languages.split(",")
skills = [language.strip() for language in skills]
user_info["skills"] = skills


# 2. Sort favourite meals alphabetically

user_info["favourite_meals"].sort()


# 3. Print the second-to-last favourite meal

print("Second-to-last meal:", user_info["favourite_meals"][-2])

# 4. Add spaghetti to favourite meals

user_info["favourite_meals"].append("spaghetti")


# 5. Add the third and fourth elements again

user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])


# 6. Remove duplicates

user_info["favourite_meals"] = list(
    dict.fromkeys(user_info["favourite_meals"])
)


# 7. Swap the first and last elements

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0]
)


# 8. Add a new phone contact

user_info["phone_contacts"]["Adam"] = "+36301234567"


# 9. Delete Tim's old phone number

del user_info["phone_contacts"]["Tim"]


# 10. Add a person with two phone numbers

user_info["phone_contacts"]["Peter"] = [
    "+36301111111",
    "+36702222222"
]


"""
Extra 1
Print the last 3 skills in reverse order
"""

print("Last 3 skills in reverse order:", user_info["skills"][-3:][::-1])


"""
Extra 2
Rename Tim2 to Tim
"""

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")


#print the final user_info dictionary
print("\nFinal user info: ")
pprint(user_info)