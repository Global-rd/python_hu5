from pprint import pprint

name = input("Enter your name: ").strip().upper()
gender = input("Enter your gender (male/female): ").strip().lower()
age = int(input("Enter your age: "))
python_experience = int(input("Enter years of Python experience: "))

age_in_days = age * 365

pronoun = "he" if gender == "male" else "she"
possessive_pronoun = "his" if gender == "male" else "her"

professional_python = input(
    "Do you want to be a professional Python developer? (yes/no): "
).strip().lower()

developer_text = "wants" if professional_python == "yes" else "does not want"

pprint(
    f"My character is {age_in_days} days old. "
    f"{possessive_pronoun.capitalize()} name is {name} and "
    f"{pronoun} has {python_experience} years experience. "
    f"{pronoun.capitalize()} {developer_text} to be a professional Python developer!"
)