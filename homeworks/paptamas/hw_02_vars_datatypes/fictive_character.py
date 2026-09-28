# fictive_character.py

# User input
name = input("Add meg a neved: ").strip().title()
age = int(input("Add meg az életkorod: "))
python_exp = input("Hány éve foglalkozol Python-nal? ")

# Extra input (szorgalmi)
pro_choice = input("Szeretnéd, hogy a karakter profi Python fejlesztő legyen? (yes/no): ").strip().lower()

# Ternary operator
pro_status = "profi Python fejlesztő lesz" if pro_choice == "yes" else "nem lesz profi Python fejlesztő"

# Age in days
age_in_days = age * 365

# Output using f-string
print(
    f"A karakter neve: {name}, életkora: {age} év, "
    f"ami napokban kifejezve {age_in_days} nap. "
    f"Python tapasztalat: {python_exp} év. "
    f"A karakter {pro_status}."
)
