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

# 1. Ask for 4 programming languages, convert to list, add to dictionary
skills_input = input("Enter 4 programming languages separated by commas (no spaces): ")
skills_list = skills_input.split(",")
user_info["skills"] = skills_list

# 2. Sort favourite_meals alphabetically
user_info["favourite_meals"].sort()
print("Sorted meals:", user_info["favourite_meals"])

# 3. Print the second-to-last element
print("Second-to-last meal:", user_info["favourite_meals"][-2])

# 4. Add "spaghetti"
user_info["favourite_meals"].append("spaghetti")
print("After adding spaghetti:", user_info["favourite_meals"])

# 5. Add the 3rd and 4th elements again (values, not indexes)
third = user_info["favourite_meals"][2]
fourth = user_info["favourite_meals"][3]
user_info["favourite_meals"].extend([third, fourth])
print("After duplicating 3rd and 4th:", user_info["favourite_meals"])

# 6. Remove duplicates
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
print("After removing duplicates:", user_info["favourite_meals"])

# 7. Swap first and last elements
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0]
)
print("After swapping first and last:", user_info["favourite_meals"])

# 8. Add a new phone contact
user_info["phone_contacts"]["Alex"] = "+3611222333"
print("After adding Alex:", user_info["phone_contacts"])

# 9. Remove Tim (old number no longer valid)
del user_info["phone_contacts"]["Tim"]
print("After removing Tim:", user_info["phone_contacts"])

# 10. Add a person with two phone numbers
user_info["phone_contacts"]["Robert"] = ["+3630111222", "+3630222333"]
print("After adding Robert with two numbers:", user_info["phone_contacts"])

# Extra 1: Print last 3 skills in reverse order
print("Last 3 skills reversed:", user_info["skills"][-3:][::-1])

# Extra 2: Rename Tim2 to Tim
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print("After renaming Tim2 to Tim:", user_info["phone_contacts"])
