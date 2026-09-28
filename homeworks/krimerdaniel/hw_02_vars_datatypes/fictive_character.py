## This program creates a brief description of a fictive character based on user input.
# A function to validate and comvert user input to integer

def user_input_int(message1, message2):
    counter = 0
    while counter < 3:  # Allow up to 3 attempts
        counter += 1
        try:
            return int(input(message1))
            break
        except ValueError:
            print(f"Invalid input. You have {3 - counter} attempts left")
    
    else:
        print(f"Too many invalid attempts to provide your {message2}. Exiting the program.")
        exit()


# Prompting user for input data for character's name and converting it properly

characters_name = input("Please provide your name: ").strip()
characters_name = characters_name.replace(',', ' ').replace('.', ' ').replace(';', ' ')
char_name_list = characters_name.split()
char_name = ''
for item in char_name_list:
    char_name += item.capitalize()+' '
characters_name = char_name.strip()


# Prompting user for input data for character's age and validating it

characters_age = user_input_int(message1="Please provide your age: ", message2="age")*365


# Prompting user for input data for character's years of experience with Python and validating it

characters_experience =  user_input_int(message1="Please provide the number of years of experience you have with Python (round to whole number): ", message2="years of experience")


# Prompting user for input data for character's opinion on becoming a professional Python developer and validating it

counter = 0
while counter <3:   # Allow up to 3 attempts 
    characters_opinion = input("Do you want to become a professional Python developer (Yes/No): ").lower()
    counter += 1    
    if characters_opinion in ["yes", "no"]:
        if characters_opinion == "yes":
            characters_opinion = "wants"
            break
        else:
            characters_opinion = "does not want"
            break
    else:
        print(f"Invalid input, you have {3 - counter} attempts left).")
    
else:
    print("Too many invalid attempts. Exiting the program.")
    exit()


print(f"My character is {characters_age} days old. His/her name is {characters_name} and he/she has {characters_experience} years experience. He/she {characters_opinion} to become a professional Python developer.")