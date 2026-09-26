#--- data collection ---

name=(input("Please enter your name: ")).upper().strip()
age=int(input("Please enter your age: "))
phyton_exp_in_years=int(input("How many years of Phyton experience: "))

#--- number of years in days ---

age_in_days=age*365

#--- create an f-String ---

introduction = f'My character is {age_in_days} old. Her name is {name} and she has {phyton_exp_in_years} years experience.'
print (introduction)