
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

skills = input("What are your programming skills? (Give four languages in the order of your preference, separated by commas without spaces) ")

skills_list = list(skills.strip().split(","))
user_info["skills"] = skills_list

favourite_meals = sorted(user_info["favourite_meals"])
user_info["favourite_meals"] = favourite_meals

from pprint import pprint
pprint(user_info)

print(favourite_meals[-2])

favourite_meals.append("spaghetti")
favourite_meals.append("sushi")
favourite_meals.append("spaghetti")

print(favourite_meals)

favourite_meals = list(set(favourite_meals))

print(favourite_meals)

favourite_meals[0], favourite_meals[-1] = favourite_meals[-1], favourite_meals[0]

print(favourite_meals)

user_info["phone_contacts"]["Cartman"] = "+36301234567"

print(user_info["phone_contacts"])

del user_info["phone_contacts"]["Tim"]

print(user_info["phone_contacts"])

user_info["phone_contacts"]["Eric"] = ["+36301333567", "+36304441567"]

print(user_info["phone_contacts"])

print(user_info["skills"][-1:-4:-1])

#user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

print(user_info["phone_contacts"])