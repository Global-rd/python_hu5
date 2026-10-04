"""

"""

name = input("What is your character's name? ").strip().capitalize()
age = int(input("How old is your character? "))
python_exp_in_years = int(input("How many years of Python experience does your character have? "))

wants_to_be_developer = input("Does your character want to be a Python developer? (yes/no)")

developer_text = "wants" if wants_to_be_developer == "yes" else "does not want"

age_in_days = age * 365

text = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} year(s) experience. He/she {developer_text} to be a developer!"

print(text)
