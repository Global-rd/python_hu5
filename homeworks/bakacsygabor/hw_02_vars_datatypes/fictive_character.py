"""Create and display a fictional character from user input."""


# input() always returns a string. strip() removes surrounding spaces,
# while upper() stores the name using uppercase letters.
character_name = input("Character name: ").strip().upper()

# int() converts the entered age from string to integer.
age_in_years = int(input("Character age in years: "))

# 365 days gives an approximate age because leap years are not considered.
age_in_days = age_in_years * 365

# float() also accepts partial years, for example 1.5 years of experience.
python_experience_in_years = float(
    input("Python experience in years: ")
)

# The homework asks for "yes" or "no". lower() makes YES and Yes work too.
wants_to_be_python_developer = input(
    "Should the character be a professional Python developer? (yes/no): "
).strip().lower()

# A ternary expression chooses one of the two sentences in a single line.
developer_message = (
    "He/she wants to be a Python developer!"
    if wants_to_be_python_developer == "yes"
    else "He/she does not want to be a Python developer!"
)

# :g displays 2.0 as 2, while still allowing values such as 1.5.
print(
    f"My character is {age_in_days} old. "
    f"His/her name is {character_name} and he/she has "
    f"{python_experience_in_years:g} years experience. "
    f"{developer_message}"
)
