# fictive_character.py

# User input
name = input("Please enter your name: ").strip().title()
age = int(input("Please enter your age: "))
python_exp = input("How many years have you been learning Python? ")

# Extra task input
pro_choice = input("Would you like your character to become a professional Python developer? (yes/no): ").strip().lower()

# Ternary operator (minimal duplication)
pro_status = "" if pro_choice == "yes" else "not"

# Age in days (assuming today is the character's birthday)
age_in_days = age * 365

# Final output using f-string
print(
    f"Character name: {name}, age: {age} years, "
    f"which is approximately {age_in_days} days old. "
    f"Python experience: {python_exp} years. "
    f"The character will {pro_status} become a professional Python developer."
)
