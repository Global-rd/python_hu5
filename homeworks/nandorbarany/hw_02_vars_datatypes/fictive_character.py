#fictive_character.py

name = input("What is your full name? ")
age = int(input("How old are you? "))
python_xp_years = int(input("How many years of Python experience do you have? "))    
question = input("Would you like your character to be a professional Python developer? ")

name = name.strip().title()
age_in_days = int(age * 365)

if question.lower().strip() == "yes":
    print(f"My character is {age_in_days} days old. His name is {name} and he has {python_xp_years} years experience in Python. He wants to be a professional Python developer.")
else:
    print(f"My character is {age_in_days} days old. His name is {name} and he has {python_xp_years} years experience in Python. He does not want to be a professional Python developer.")
