# 1. Feladat: Adatok bekérése
# A .strip() eltávolítja a szóközöket az elejéről/végéről, a .title() nagy kezdőbetűssé teszi a szavakat
name = input("Add meg a karakter nevét: ").strip().title()
age = int(input("Add meg a karakter életkorát (években): "))
python_exp_in_years = input("Python tapasztalat években: ")

# Extra feladat (szorgalmi): Karakter fejlesztői szándéka
wants_to_be_dev_input = input("Szeretné, hogy a karaktere profi Python fejlesztő legyen? (yes/no): ").strip().lower()

# Életkor kiszámítása napokban (365 nappal számolva)
age_in_days = age * 365

# Szorgalmi feladat megoldása a DRY elv alapján (csak a változó részt tároljuk)
dev_status = "wants" if wants_to_be_dev_input == "yes" else "does not want"

# Végeredmény kiíratása f-string használatával (az oktató által kért rövidebb, tiszta formátumban)
print(
    f"My character is {age_in_days} days old. His/her name is {name} "
    f"and he/she has {python_exp_in_years} years experience. He/she {dev_status} to be a Python developer!"
)
