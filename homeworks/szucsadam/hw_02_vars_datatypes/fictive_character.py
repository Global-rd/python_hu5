first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()
age = int(input("Age: "))
python_experience = int(input("Python experience (in years): "))

# name = first_name + " " + last_name
name = f"{first_name} {last_name}".upper()

age_in_days = age * 365

"""
print(name)
print(age)
print(python_experience)
print(age_in_days)
"""

print(f"My character is {age_in_days} days old and has {python_experience} years of Python experience. His name is {name}.")


