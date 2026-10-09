#fictive_character.py

name = input("What is your full name? ").strip().title()
age = int(input("How old are you? "))
python_xp_years = int(input("How many years of Python experience do you have? "))    
question = input("Would you like your character to be a professional Python developer? ")

age_in_days = age * 365

if question.lower().strip() == "yes":
    dev_ambition = "wants"
else:
    dev_ambition = "does not want"

print(f"My character is {age_in_days} days old. His name is {name} and he has {python_xp_years} years experience in Python. He {dev_ambition} to be a professional Python developer.")

