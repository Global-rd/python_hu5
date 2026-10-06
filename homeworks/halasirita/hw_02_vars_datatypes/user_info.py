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

# 1
skills_list = input(
    "List 4 programming languages (language1,language2,language3,language4): "
)

skills = skills_list.split(",")

user_info["skills"] = skills

# 2

user_info["favourite_meals"].sort()

# 3

print(user_info["favourite_meals"][-2])

# 4
user_info["favourite_meals"].append("spaghetti")

# 5

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# 6

user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))

# 7

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

# 8

user_info["phone_contacts"]["Joska Pista"] = "+3618765432"

# 9

del user_info["phone_contacts"]["Tim"]


# 10

user_info["phone_contacts"]["Damien"] = ["+36709876789", "+36301231234"]
print(user_info["phone_contacts"])



# 1. extra 1

print(user_info["skills"][:-4:-1])

# 2. extra

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
