#Homwework_02_datatypes

#1_exercise

#My_Character:
#Name:    pettendi attila     
#Age:42.8
#Python_Experiance:0.1
"""
format_name = input("What is your name? ").title().strip()
age = float(input("How old are you? "))
age_in_days = round(age*365)
python_experiance = float(input("Years of experience with Python? "))
python_exp_in_years = round(python_experiance)
print("-"*80)
print(f"My character is {age_in_days} days old. His/Her name is {format_name} and he/she has {python_exp_in_years} years experience.")
"""


#1_extra_exercise

format_name = input("What is your name? ").title().strip()
gender = input("What is your gender? ").title().strip()
gender_pos = "his" if gender == "he" else "her"
gender_sub = "he" if gender == "he" else "she"
age = float(input("How old are you? "))
age_in_days = round(age*365)
python_experiance = float(input("Years of experience with Python? "))
python_exp_in_years = round(python_experiance)
do_you_want_dev = input("Do you want to be a Python developer? (yes/no): ")
format_do_you_want_dev = do_you_want_dev.strip()
dev_status = "wants" if format_do_you_want_dev == "yes" else "does not want"
print("-"*80)
print(f"My character is {age_in_days} days old. {(gender_pos.capitalize())} name is {format_name} and {gender_sub} has {python_exp_in_years} years experience. {(gender_sub.capitalize())} {dev_status} to be Python developer")
