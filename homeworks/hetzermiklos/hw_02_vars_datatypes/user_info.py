"""
Homework 2 - Variables and data types
Task 2 - List and dictionary operations
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

# 1. Ask for 4 programming languages and add them as "skills"
skills = input(
    "Enter 4 programming languages separated by commas without spaces: "
).split(",")

user_info["skills"] = skills

# 2. Sort favourite meals alphabetically
user_info["favourite_meals"].sort()

# 3. Print the second to last favourite meal
print(user_info["favourite_meals"][-2])

# 4. Add spaghetti
user_info["favourite_meals"].append("spaghetti")

# 5. Add the third and fourth elements again
user_info["favourite_meals"].extend(
    user_info["favourite_meals"][2:4]
)

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
user_info["phone_contacts"]["John"] = "+36123456789"

# 9. Delete the old Tim contact
del user_info["phone_contacts"]["Tim"]

# 10. Add a person with two phone numbers
user_info["phone_contacts"]["Anna"] = [
    "+36201234567",
    "+36301234567"
]

# Extra 1: Print the last 3 skills in reverse order
print(user_info["skills"][-3:][::-1])

# Extra 2: Rename Tim2 to Tim
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

# Print the final dictionary
print(user_info)
