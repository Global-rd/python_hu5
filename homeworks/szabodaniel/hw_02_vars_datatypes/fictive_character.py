name = (input("What is your name?")
        .capitalize()
        .strip())

print(name)
print(type(name))


age = input("Your age?")
age_in_days = int(age) * 365

print(age_in_days)

python_exp_in_years = input("Years of Python experience?")

information = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience."
print(information)