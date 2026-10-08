name = input("Whats your name?: ").upper().strip()
age = int(round(float(input("How old are you?: ").replace(",", "."))))
python_exp_in_years = int(input("Python experience in years?: "))

age_in_days= age * 365

print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")

pro = input("Do you want to become a professional Python developer?")

pro_answer = "want" if pro == "yes" else "don't want"

print(f"My character is {age} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she {pro_answer} to be a Python developer!")