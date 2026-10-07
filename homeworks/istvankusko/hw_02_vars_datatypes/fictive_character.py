#fictive_character.py
print("This is Homework 2\n")
character_name = input("What your name? :") # name input
character_name_str = character_name.upper().strip()

character_age = input("How old are you? : ")
character_age_int = int(character_age)

character_experience = input("How many years of Python experience do you have? :")
character_experience_int = int(character_experience)
"""
How could this be done even better?
"""
character_pro = input("Would you like to become a professional Python developer? yes/no :")
character_pro_bool = True if character_pro.strip().lower() == "yes" else False
character_pro_text = "wants" if character_pro_bool else "does not want"


print("\n")
print(f"My character is {character_age_int} old. His/her name is {character_name_str} and he/she has {character_experience_int} years experience. He/she {character_pro_text} to be a Python developer!\n")


