"""Practise list and dictionary operations with user information."""


user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi",
    ],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    },
}


# 1. split(",") converts the comma-separated string into a list.
programming_languages = input(
    "Enter four programming languages separated by commas without spaces: "
).split(",")
user_info["skills"] = programming_languages

# 2. sort() changes the existing list into ascending alphabetical order.
user_info["favourite_meals"].sort()

# 3. Index -2 selects the second-to-last item.
print("Sorted favourite meals:", user_info["favourite_meals"])
print("Second-to-last favourite meal:", user_info["favourite_meals"][-2])

# 4. append() adds one new item to the end of the list.
user_info["favourite_meals"].append("spaghetti")

# 5. Slice [2:4] selects the current third and fourth items.
user_info["favourite_meals"].extend(
    user_info["favourite_meals"][2:4]
)

# 6. Dictionary keys are unique, so this removes duplicates while
# preserving the original order of the list.
user_info["favourite_meals"] = list(
    dict.fromkeys(user_info["favourite_meals"])
)

# 7. Multiple assignment swaps the first and last items.
favourite_meals = user_info["favourite_meals"]
favourite_meals[0], favourite_meals[-1] = (
    favourite_meals[-1],
    favourite_meals[0],
)

# 8. Add one new name and phone number to the nested dictionary.
user_info["phone_contacts"]["Anna"] = "+36705551234"

# 9. Delete Tim's outdated contact entry.
del user_info["phone_contacts"]["Tim"]

# 10. A list stores two phone numbers under one person's name.
user_info["phone_contacts"]["Peter"] = [
    "+36305550101",
    "+36305550102",
]

# Extra 1. Take the last three skills, then reverse their order.
print("Last three skills in reverse order:", user_info["skills"][-3:][::-1])

# Extra 2. pop() removes Tim2 and returns its value under the new Tim key.
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop(
    "Tim2"
)

print("Final favourite meals:", user_info["favourite_meals"])
print("Final phone contacts:", user_info["phone_contacts"])
