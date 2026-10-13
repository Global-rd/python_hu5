# getting user input
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_python_experience = input("Enter your Python experience (in years)): ")
user_motivation = input("Do you want to be a Python expert? (yes/no): ")

# no spaces, capitalize
user_name_capitalized = user_name.strip().capitalize()
# transform string to int and calculate age in days
user_age_number = int(user_age)
user_age_day = user_age_number * 365
#Ternary operator to check motivation
user_motivation_lowercase = user_motivation.strip().lower()
user_motivation_output = "He/she wants to be a Python developer!" if user_motivation_lowercase == "yes" else "He/she does not want to be a Python developer."

# print results by using f-string
print(f"My character is {user_age_day} days old. His/her name is {user_name_capitalized} and he/she has {user_python_experience} years of Python experience.")
print(user_motivation_output)
