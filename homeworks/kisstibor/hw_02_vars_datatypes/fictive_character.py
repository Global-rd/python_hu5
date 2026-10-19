#  2. Házi feladat / Feladat 1. Változók, user input, string metódusok, type conversion, f-string használata

# MODUL IMPORTÁLÁS
from datetime import datetime  # datetime modul importálása a dátumok műveletek használatához

# AKTUÁLIS DÁTUM ÉS IDŐ BEOLVASÁSA
now_date = datetime.now() # Mai dátum és idő kiírása a now_date változóba

# Név bekérése , tárolása csupa nagybetűvel és szóköz tisztítással
name = (input("Enter your name: ")).upper().strip()
print(f"   Name: {name}, Length: {len(name)}, Type: {type(name)}")

# Életkor bekérése és tárolása integer típusban 
age = int(input("Enter your age: "))

# Életkor napokban történő kiszámítása
age_in_days = (now_date - now_date.replace(year=now_date.year - age)).days
print(f"   Age: {age} years(s), that in days: {age_in_days}, Type: {type(age)}")
'''
    Magyarázat a age_in_days kiszámításához:
    1. Születési dátum kiszámítása (szökőévvekkel is számolva):
        ~ now_date.year       : Lekéri a jelenlegi évet (pl. 2026).
        ~ - age               : Kivonja belőle az életkort (pl. 2026 - 20 = 2006).
        ~ .replace(year=...)  : Lecseréli a jelenlegi évet a számított születési évre, 
                                miközben a hónapot és a napot változatlanul hagyja.
    2. Életkor átszámítása napokba:
        ~ (now_date - birth_date).days : Kivonja a születési dátumot a jelenlegi dátumból, 
                                        és a különbséget pontosan napokban adja vissza.
'''

# Pythion tapasztalat bekérése és tárolása integer típusban
python_experience_in_years = int(input("Enter your Python experience in years: "))  
print(f"   Experience value: {python_experience_in_years}, Type: {type(python_experience_in_years)}") 

message = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_experience_in_years} years experience."
print(message)

# Extra feladat (szorgalmi):

# Kérdés a Python fejlesztői választásról
yes_or_no = input("Does he/she want to be a Python developer? (yes/no): ").lower().strip()

# Megoldás 1a: if-else szerkezet használatával
if yes_or_no == "yes":
    message = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_experience_in_years} years experience. He/she wants to be a Python developer!"
else:
    message = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_experience_in_years} years experience. He/she does not want to be a Python developer!"
print(message)

# Megoldás 1b: if-else szerkezet használatával 
if yes_or_no == "yes":
    sub_message = "wants" 
else:
    sub_message = "does not want"

message = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_experience_in_years} years experience. He/she {sub_message} to be a Python developer!"
print(message)

# Megoldás 2: Ternary operator használatával
message = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_experience_in_years} years experience. He/she {'wants' if yes_or_no == 'yes' else 'does not want'} to be a Python developer!"
print(message)

