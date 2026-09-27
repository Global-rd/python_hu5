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

input_program_languages = [input("program_language_1"),input("program_language_2"),input("program_language_3"),input("program_language_4")]
print(input_program_languages)

user_info["skills"] = input_program_languages #1. add skills
pprint(user_info)

user_info["favourite_meals"].sort() #2. abc rendezes

print(user_info["favourite_meals"][-2]) #3. urolso elotti elem

user_info["favourite_meals"].append("spagetti") #4. add spagetti
print(user_info["favourite_meals"])

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4]) #5. add utolso ket elem
print(user_info["favourite_meals"])

user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) #6. duplikatumok torlese
print(user_info["favourite_meals"])

favourite_meals_first = user_info["favourite_meals"][0]
favourite_meals_last = user_info["favourite_meals"][-1]
user_info["favourite_meals"][0] = favourite_meals_last
user_info["favourite_meals"][-1] = favourite_meals_first #7. elso es utolso elem csere

print(user_info["favourite_meals"])
