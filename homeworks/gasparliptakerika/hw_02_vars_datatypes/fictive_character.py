
name = input("Kérlek add meg a neved! ") 
age = int(input("Hány éves vagy? "))
python_exp_in_years = int(input("Hány éve foglalkozol Python programozással? "))

age_in_days = age * 365
name_good = name.strip().title()

introduction = f"My character is {age_in_days} old. His/her name is {name_good} and he/she has {python_exp_in_years} years experience."
print(introduction)