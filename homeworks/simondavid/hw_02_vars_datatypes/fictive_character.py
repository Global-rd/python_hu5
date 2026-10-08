
# Homework 02 - Task 1
# Fictional character - Simon David

# Asking for user information
name = input("Enter your character's name: ").strip().upper()
age = int(input("Enter your character's age: "))
python_experience = float(input("Years of Python experience: "))

# Converting age to days (365 days per year)
age_in_days = age * 365

# Extra task - ternary operator
developer_answer = input(
    "Does your character want to be a Python developer? (yes/no): "
).strip().lower()

developer_status = (
    "wants to be a Python developer!"
    if developer_answer == "yes"
    else "does not want to be a Python developer!"
)

# Display character information using an f-string
print(
    f"My character is {age_in_days} days old. "
    f"His/her name is {name} and he/she has "
    f"{python_experience} years experience. "
    f"He/she {developer_status}"
)
