## This program creates a brief description of a fictive character based on user input.

# Prompting user for input data for character's name and converting it properly

characters_name = input("Please provide your name: ").strip()
characters_name = characters_name.replace(',', ' ').replace('.', ' ').replace(';', ' ')
char_name_list = list(characters_name.split())
char_name = ''
for item in char_name_list:
    char_name += item.capitalize()+' '
characters_name = char_name.strip()


# Prompting user for input data for character's age and validating it

characters_age = input("Please provide your age: ")
counter = 0
while counter < 3:  # Allow up to 3 attempts
    counter += 1
    try:
        characters_age = int(characters_age)*365
        break
    except ValueError:
        characters_age = input(f"Invalid input. Please provide your age as a whole number (you have {3 - counter} attempts left): ")
   
else:
    print("Too many invalid attempts to provide your age. Exiting the program.")
    exit()


# Prompting user for input data for character's years of experience with Python and validating it

characters_experiance = input("Please provide the number of years of experience you have with Python (round to whole number): ")
counter = 0
while counter < 3:  # Allow up to 3 attempts
    counter += 1
    try:
        characters_experiance = int(characters_experiance)
        break
    except ValueError:
        characters_experiance = input(f"Invalid input. Please provide the number of years of experience you have with Python as a whole number (you have {3 - counter} attempts left): ")
   
else:
    print("Too many invalid attempts to provide years of experience. Exiting the program.")
    exit()


# Prompting user for input data for character's opinion on becoming a professional Python developer and validating it

characters_opinion = input("Do you want to become a professional Python developer (Yes/No): ").lower()
counter = 0
while counter < 3:  # Allow up to 3 attempts
    counter += 1
    if characters_opinion in ["yes", "no"]:
        if characters_opinion == "yes":
            characters_opinion = "wants"
        else:
            characters_opinion = "does not want"
        break
    else:
        if counter < 3:
            characters_opinion = input(f"Invalid input. Please provide 'Yes' or 'No' (you have {3 - counter} attempts left): ").lower()
else:
    print("Too many invalid attempts. Exiting the program.")
    exit()


print(f"My character is {characters_age} days old. His/her name is {characters_name} and he/she has {characters_experiance} years experience. He/she {characters_opinion} to become a professional Python developer.")