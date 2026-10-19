name = input("What is your full name? ").title().strip()
age = int(input("How old are you? "))
python_experience_in_years = int(input("How many years of experience do you have with Python? "))

age_in_days = int(age*365)

introduction = f"My character is {age_in_days} old. His name is {name} and has {python_experience_in_years} years experience"
print(introduction)

#extra 1
python_developer = input("Would you like to be a Python developer? (yes/no) ").lower().strip()
print(f"My character is {age_in_days}old. His name is {name} and he has {python_experience_in_years} years experience. He {'wants' if python_developer == 'yes' else 'does not want'} to be a Python developer.")