
import nt
from pprint import pprint

print("Enter four programming languages.")

programming_language_1 = input("Enter a programming language 1: ").strip()
programming_language_2 = input("Enter a programming language 2: ").strip()
programming_language_3 = input("Enter a programming language 3: ").strip()
programming_language_4 = input("Enter a programming language 4: ").strip()

programming_language_list = [programming_language_1, programming_language_2, programming_language_3, programming_language_4]

# print(programming_language_list)


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
    },
    "programming_language_list": [[
        [programming_language_1], 
        [programming_language_2], 
        [programming_language_3], 
        [programming_language_4]
    ]]
}

user_info["favourite_meals"].sort() # abc szerint sorba

print(user_info["favourite_meals"])

print(user_info["favourite_meals"][-2]) # utolsó előtti elem






