import os
os.system("cls")
import pprint

# Original data
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


# Prompting user for 4 'skills' items separated by comma; validating and forming the input accordingly
user_skills = input("Please provide exactly 4 skills separated by commas: ")
user_skills = list(user_skills.replace(' ', '').replace('.', ',').replace(';', ',').replace('-', ',').split(","))
counter = 0
while counter < 2:  # Allow up to 3 attempts
    counter += 1
    if len(user_skills) == 4:
           break
    else:
        user_skills = input(f"Your input is not EXACTLY 4 skills. Please provide EXACTLY 4 skills separated by commas (you have {3 - counter} attempts left): ")
else:
    print("Too many invalid attempts to provide EXACTLY 4skills. Exiting the program.")
    exit()
user_info["skills"] = user_skills
print(user_info["skills"])


# Arranging ites in 'favourite_meals in alphabetical order
user_info["favourite_meals"].sort()


# Printing the second to last item of the 'favourite_meals' list, as well as the entire list
print(f'The second to last item of the "favourite_meals" list is: {user_info["favourite_meals"][-2]}')
print(f'The entire "favourite_meals" list is: {user_info["favourite_meals"]}')


# Adding 'spaghetti' to the 'favourite_meals' list
user_info["favourite_meals"].append("spaghetti")
print(f'The entire "favourite_meals" list is: {user_info["favourite_meals"]}')


# Adding the 3rd and the 4th items of the 'fvourite_meals' to the favourite_meals' list
temp_fav_meals = user_info["favourite_meals"]
for i in range(2, 4):
    temp_fav_meals.append(user_info["favourite_meals"][i])
user_info["favourite_meals"] = temp_fav_meals
del temp_fav_meals
print(f'The entire "favourite_meals" list is: {user_info["favourite_meals"]}')


# Removing duplicates from the 'favourite_meals' list
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(f'The entire "favourite_meals" list is: {user_info["favourite_meals"]}')


# Swapping the first and last items of the 'favourite_meals' list
temp_fav_meals = user_info["favourite_meals"]
temp_fav_meals[0], temp_fav_meals[-1] = temp_fav_meals[-1], temp_fav_meals[0]
user_info["favourite_meals"] = temp_fav_meals
del temp_fav_meals
print(f'The entire "favourite_meals" list is: {user_info["favourite_meals"]}')


# Adding a new contact to the 'phone_contacts' dictionary
user_info["phone_contacts"]["Jackie"] = "+36209998877"
pprint.pprint(user_info["phone_contacts"])


# Removing "Tim" from the 'phone_contacts' dictionary
user_info["phone_contacts"].pop("Tim")
pprint.pprint(user_info["phone_contacts"])


#Adding a new contact having two phone numbers to the 'phone_contacts' dictionary
user_info["phone_contacts"]["Jack"] = "+36209876543"
user_info["phone_contacts"]["Jack_2"] = "+36201234567"
pprint.pprint(user_info["phone_contacts"])


# Printing the last 3 items of the 'skills' list in reverse order
print(f"The last 3 items of the 'skills' list in reverse order are: {user_info['skills'][-3:][::-1]}")


# 'Renaming' the key "Tim2" to "Tim" in the 'phone_contacts' dictionary
tim = user_info["phone_contacts"].get("Tim2")
user_info["phone_contacts"].pop("Tim2")
user_info["phone_contacts"]["Tim"] = tim
pprint.pprint(user_info["phone_contacts"])

print(


)
pprint.pprint(user_info)
