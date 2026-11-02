# Adatbekérés a felhasználótól
name = input("Mi a karaktered neve? ").strip().title()
age = input("Hány éves? ")
age_in_days = round(float(age) * 365)
python_exp = input("Hány év Python-tapasztalata van? ")

# Kiíratás
print(f"My character is {age_in_days} days old."
      f" His/her name is {name} and he/she has {python_exp} years experience.")

# szeretne-e Python fejlesztő lenni
answer = input("Szeretnéd, hogy a karaktered profi Python fejlesztő legyen? (yes/no) ")
developer_text = "wants to be" if answer == "yes" else "does not want to be"

# Kiírás f-stringgel
print(f"My character is {age_in_days} days old."
      f" His/her name is {name} and he/she has {python_exp} years experience."
       f" He/she {developer_text} a Python developer!")