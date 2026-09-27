name = input("Kérlek add meg a neved: ").title().strip()
age = int(input("Kérlek add meg a korod: "))
python_exp_in_years = int(input("Hány éve foglalkozol Python-nal? "))

age_in_days = age * 365

print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")
