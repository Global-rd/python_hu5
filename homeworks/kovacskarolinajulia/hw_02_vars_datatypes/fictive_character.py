name = input("Név: ").strip().upper()
age = int(input("Életkor: "))
python_exp = int(input("Hány év Python tapasztalata van: "))
age_in_days = age * 365

print(
    f"My character name is {age_in_days}"
    f"His/Her name is {name} and he/she has {python_exp} years experience."
)