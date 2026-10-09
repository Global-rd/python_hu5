
# Homework 02 - Task 2
# List and dictionary operations - Simon David

# Original user information
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

# Task 1 - Ask for four programming languages
skills_input = input(
    "Enter 4 programming languages separated by commas: "
)
user_info["skills"] = skills_input.split(",")

print("Skills:", user_info["skills"])

# Task 2 - Sort favourite meals alphabetically
user_info["favourite_meals"].sort()
print("Sorted meals:", user_info["favourite_meals"])

# Task 3 - Print the second-to-last meal
print("Second-to-last meal:", user_info["favourite_meals"][-2])

# Task 4 - Add spaghetti to favourite meals
user_info["favourite_meals"].append("spaghetti")

# Task 5 - Duplicate the third and fourth meals
user_info["favourite_meals"].extend(
    user_info["favourite_meals"][2:4]
)
print("Meals with duplicates:", user_info["favourite_meals"])

# Task 6 - Remove duplicates while preserving order
user_info["favourite_meals"] = list(
    dict.fromkeys(user_info["favourite_meals"])
)
print("Meals without duplicates:", user_info["favourite_meals"])

# Task 7 - Swap the first and last meals
meals = user_info["favourite_meals"]
meals[0], meals[-1] = meals[-1], meals[0]

print("Meals after swapping:", meals)

# Task 8 - Add a new phone contact
user_info["phone_contacts"]["David"] = "+36301234567"

# Task 9 - Remove Tim's old phone number
del user_info["phone_contacts"]["Tim"]

# Task 10 - Add a contact with two phone numbers
user_info["phone_contacts"]["Alex"] = [
    "+36301112222",
    "+36703334444"
]

# Extra 1 - Print the last three skills in reverse order
print("Last 3 skills reversed:", user_info["skills"][:-4:-1])

# Extra 2 - Rename Tim2 to Tim
user_info["phone_contacts"]["Tim"] = (
    user_info["phone_contacts"].pop("Tim2")
)

# Represent final dictionary
print("\nFinal user information:")
print(user_info)
