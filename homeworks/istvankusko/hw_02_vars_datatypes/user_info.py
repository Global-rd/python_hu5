#user_info.py

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

print("----------------------------------------------------------------")
print(f"The second-to-last item in the “favorite_meals” list:  {user_info["favourite_meals"][-2]}")
print("----------------------------------------------------------------")
# Add spaghetti to the favourite_meals list.
print(f"Add spaghetti to the favourite_meals list. ")
user_info["favourite_meals"].append("spaghetti")
print("----------------------------------------------------------------")
skills_input = input("List 4 programming languages, separated by commas, without spaces: ")
user_info["skills"] = skills_input.split(",")
print("----------------------------------------------------------------")
print(user_info["favourite_meals"])
print("----------------------------------------------------------------")
# add to favourite_meals 2 itmes
print(f"add to favourite_meals 2 itmes \n")
user_info["favourite_meals"].append(user_info["favourite_meals"][1])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])
print(f"After expanding the list:: \n {user_info["favourite_meals"]} \n")
print("----------------------------------------------------------------")
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(f"After deleting duplicates: \n {user_info["favourite_meals"]}")
print("----------------------------------------------------------------")
print(f"-----------------order swap--------------------\n")
(
    user_info["favourite_meals"][0],
    user_info["favourite_meals"][-1],
) = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0],
)
print(user_info["favourite_meals"])
print("----------------------------------------------------------------")
user_info["phone_contacts"]["O'Connell"] = "+367048762343"
print(user_info["phone_contacts"])
print("----------------------------------------------------------------")
user_info["phone_contacts"]["Tim"] = None
print(f"contact list after we deleted Tim's cell phone number.: \n {user_info["phone_contacts"]}")
print("----------------------------------------------------------------")
user_info["phone_contacts"]["Kate"] = ["+36301112233", "+36704445566"]