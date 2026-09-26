from pprint import pprint

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

# 1. task
skills = input("Enter 4 programming languages: ")
skills = skills.split(",")
user_info.update({"skills": skills})

#pprint(user_info)

# 2. task
user_info["favourite_meals"] = sorted((user_info["favourite_meals"]))

# 4. task
pprint(user_info["favourite_meals"][-2])

# 5. task
user_info["favourite_meals"].append("spaghetti")

# 6. task
more_favourite_meals = user_info["favourite_meals"][2],user_info["favourite_meals"][3]
#print(more_favourite_meals)

user_info["favourite_meals"].extend(more_favourite_meals)
#pprint(user_info)

# 7. task
user_info["favourite_meals"] = sorted(list(set(user_info["favourite_meals"])))
pprint(user_info)

# 8. task
user_info["favourite_meals"][0],user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
pprint(user_info)


# 9. task

user_info["phone_contacts"]["Amy"] = "+36702345678"
pprint(user_info["phone_contacts"])


# 10. task 
del user_info["phone_contacts"]["Tim"] 
pprint(user_info["phone_contacts"])

# 11. task 
user_info["phone_contacts"]["Emily"] = ["+36702345678","+36309875432"]
pprint(user_info["phone_contacts"])

# 12 task
pprint(user_info["skills"])
pprint(user_info["skills"][-3:][::-1])

# 13 task
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint(user_info["phone_contacts"])

