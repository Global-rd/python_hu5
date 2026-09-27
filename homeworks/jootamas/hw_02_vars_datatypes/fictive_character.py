name = input("Kérlek add meg a neved: ").title().strip()
age = int(input("Kérlek add meg a korod: "))
python_exp_in_years = int(input("Hány éve foglalkozol Python-nal? "))

age_in_days = age * 365

# extra 1

want_to_be_professional = input("Szeretnéd, hogy a karaktered professzionális Python fejlesztő legyen? (yes/no): ").lower().strip()

# result
# a ket kulon valtozo csak az olvashatosag miatt, hogy ne legyen tul hosszu a print egy sorban

result_string_1 = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience."
result_string_2 = f"He/she {'' if want_to_be_professional == 'yes' else 'does not '}wants to be a professional Python developer!"

print(f"{result_string_1} {result_string_2}")
