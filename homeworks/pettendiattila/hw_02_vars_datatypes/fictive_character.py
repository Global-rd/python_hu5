#Homwework_02_datatypes

#1_exercise

#My_Character:
#Name:    pettendi attila     
#Age:42.8
#Python_Experiance:0.1
"""
name = input("What is your name? ")
format_name = (name.title().strip())
age = float(input("How old are you? "))
age_in_days = round(age*365)
python_experiance = float(input("Years of experience with Python? "))
python_exp_in_years = round(python_experiance)
print("-"*80)
print(f"My character is {age_in_days} days old. His name is {format_name} and he has {python_exp_in_years} years experience.")
"""


#1_extra_exercise

name = input("What is your name? ")
gender = input("What is your gender? ")
format_gender = (gender.title().strip())
gender_pos = "his" if gender == "he" else "her"
gender_sub = "he" if gender == "he" else "she"
format_name = (name.title().strip())
age = float(input("How old are you? "))
age_in_days = round(age*365)
python_experiance = float(input("Years of experience with Python? "))
python_exp_in_years = round(python_experiance)
do_you_want_dev = input("Do you want to be a Python developer? (yes/no): ")
format_do_you_want_dev = (do_you_want_dev.strip())
dev_status = "wants to be a Python developer!" if format_do_you_want_dev == "yes" else "does not want to be a Python developer!"
print("-"*80)
print(f"My character is {age_in_days} days old. {(gender_pos.capitalize())} name is {format_name} and {gender_sub} has {python_exp_in_years} years experience. {(gender_sub.capitalize())} {dev_status}")
