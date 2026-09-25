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

#1
programming_languages_input = input("Please enter 4 programming languages (comma-separated, no spaces):") #Python,JavaScript,Java,C++
#print(programming_languages_input)
skills = programming_languages_input.split(",")
#print(skills)
user_info.update({"skills": skills})
#print(user_info)

#2
user_info["favourite_meals"].sort()
#print("Sorted favourite meals:", user_info["favourite_meals"])

#3
print(user_info["favourite_meals"][-2])

#4
user_info["favourite_meals"].append("spaghetti")
print("Extended favourite meals:", user_info["favourite_meals"])

#5
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print("Duplicated favourite meals:", user_info["favourite_meals"])

#6
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print("Removed duplicated favourite meals:", user_info["favourite_meals"]) # itt most megvaltozik a sorrend, mert a set nem garantálja az elemek sorrendjét

#7
user_info["favourite_meals"][0],user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0]
)
print("Swapped first and last favourite meals:", user_info["favourite_meals"])

#8
user_info["phone_contacts"].update({"John": "+36123456789"})
print("Updated phone contacts:", user_info["phone_contacts"])

#9
user_info["phone_contacts"].pop("Tim")
print("Removed Tim from phone contacts:", user_info["phone_contacts"])

#10
user_info["phone_contacts"].update({"Alex": {"work": "+36709876543", "personal": "+36201234567"}})
print("Added Alex with work and personal numbers:", user_info["phone_contacts"])


# Extra 1:
print("Last 3 skills reversed", user_info["skills"][-1:-4:-1])

#Extra 2:
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
user_info["phone_contacts"].pop("Tim2")
print("Updated Tim", user_info["phone_contacts"])

print("Final user info:")
pprint(user_info)


