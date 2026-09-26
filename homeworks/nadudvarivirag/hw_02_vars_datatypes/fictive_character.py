# Entering the user name
name = input("Enter your name: ")
name = name.title().strip()

# Entering the user age
age = input("Enter your age: ")
age = int(age)
age_in_days = 365*age

# Entering the experience
python_experience = input("Enter your Python experiencce in years: ")


# Entering intention
answer = input("Would you like to be a professional python developer? ")

if answer == "Yes" or "yes" :
    print(f"My character is {age_in_days} old in days. Her name is {name} and she has {python_experience} years experience in Python programming language. She want to be a professional developer ")
else: print(f"My character is {age_in_days} old in days. Her name is {name} and she has {python_experience} years experience in Python programming language. She doesn't want to be a professional developer")