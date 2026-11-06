"""
Homework 2 - Variables and data types
Task 1 - Fictive character
"""

name = input("Enter your character's name: ").strip().upper()
age = int(input("Enter your character's age: "))
python_exp_in_years = float(input("Enter Python experience in years: "))

age_in_days = age * 365

developer_answer = input(
    "Does your character want to be a professional Python developer? (yes/no): "
).strip().lower()

developer_text = (
    "He/she wants to be a Python developer!"
    if developer_answer == "yes"
    else "He/she does not want to be a Python developer!"
)

print(
    f"My character is {age_in_days} days old. "
    f"His/her name is {name} and he/she has "
    f"{python_exp_in_years} years experience. "
    f"{developer_text}"
)
