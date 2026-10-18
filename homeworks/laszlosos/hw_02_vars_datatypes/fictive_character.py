name = input("What is your name? ")
name = name.upper().strip()
age = input("How old is your character? ")
age = int(age)
age_in_days = age * 365
python_exp_in_years = input("How many years of experience do you have in Python? ")
developer = input("Do you want to be a professional Python developer?")
developer = developer.lower().strip()
answer = "wants" if developer == "yes" else "does not want" 
introduction = f"My character is {age_in_days} days old. His name is {name} and he has {python_exp_in_years} years experience. He {answer} to be a developer" 
print(introduction)



