# Entering the user name
name = input("Enter your name: ").title().strip()


# Entering the user age
age = int(input("Enter your age: "))
age_in_days = 365*age

# Entering the experience
python_experience = input("Enter your Python experiencce in years: ")


# Entering intention
answer = input("Would you like to be a professional python developer? ").lower()

dev_motivation = "wants" if answer.lower() == "yes" else "does not want"


print(f"My character is {age_in_days} old in days. Her name is {name} and she has {python_experience} years experience in Python programming language. She {dev_motivation} to be a professional developer ")
