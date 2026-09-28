name = input("Kérlek add meg a neved: ").title().strip()
age = int(input("Kérlek add meg a korod: "))
python_exp_in_years = int(input("Hány éve foglalkozol Python-nal? "))

age_in_days = age * 365

# extra 1

want_to_be_professional = input("Szeretnéd, hogy a karaktered professzionális Python fejlesztő legyen? (yes/no): ").lower().strip()

# result

character_summary = (
  f"My character is {age_in_days} days old. "
  f"His/her name is {name} and "
  f"he/she has {python_exp_in_years} years experience. "
  f"He/she {'' if want_to_be_professional == 'yes' else 'does not '}wants"
  " to be a professional Python developer!"
)

print(character_summary)

# vagy kulon valtozo nelkul

"""
print(
  f"My character is {age_in_days} days old.",
  f"His/her name is {name} and",
  f"he/she has {python_exp_in_years} years experience.",
  f"He/she {'' if want_to_be_professional == 'yes' else 'does not '}wants"
  f"to be a professional Python developer!"
)
"""
