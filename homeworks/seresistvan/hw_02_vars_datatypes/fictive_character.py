# Karakter nevének bekérése
name = input("Add meg a karakter nevét: ").strip().upper()

# Életkor és tapasztalar bekérése:
age_in_years = int(input("Add meg a karakter életkorát években: "))
python_exp_in_years = float(input("Add meg a Python-tapasztalatát években: "))

# Egyszerűsítés
age_in_days = age_in_years * 365

#Minden inó kiiratása f-stringben
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has  {python_exp_in_years} years of Python experience.")
