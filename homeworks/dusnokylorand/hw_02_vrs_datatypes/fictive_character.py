name = input("Enter your name: ").strip().upper()
age = int(input("Enter your age: "))
python_experience = int(input("Enter your Python experience in years: "))

age_in_days = age * 365

wants_to_be_developer = input(
    "Do you want your character to be a Python developer? (yes/no): "
).strip().lower()

developer_message = (
    "wants"
    if wants_to_be_developer == "yes"
    else "does not want"
)

print(
    f"My character is {age_in_days} days old. "
    f"His/her name is {name} and he/she has "
    f"{python_experience} years experience. "
    f"He/she {developer_message} to be a Python developer!"
)
