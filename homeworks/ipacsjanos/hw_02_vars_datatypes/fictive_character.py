# 1. Feladat: Adatok bekérése
# A .strip() eltávolítja a szóközöket az elejéről/végéről
# A .title() nagy kezdőbetűssé teszi a szavakat
name = input("Add meg a karakter nevét: ").strip().title()
age = int(input("Add meg a karakter életkorát (években): "))
python_exp_in_years = input("Python tapasztalat években: ")

# Extra feladat (szorgalmi): A karakter fejlesztői szándéka
wants_to_be_dev_input = input("Szeretné, hogy a karaktere profi Python fejlesztő legyen? (yes/no): ").strip().lower()

# Életkor kiszámítása napokban (365 nappal számolva)
age_in_days = age * 365

# Szorgalmi feladat megoldása Ternary Operator (háromtagú operátor) segítségével
# Szintaxisa: [érték_ha_igaz] if [feltétel] else [érték_ha_hamis]
dev_status = "He/she wants to be a Python developer!" if wants_to_be_dev_input == "yes" else "He/she does not want to be a Python developer!"

# Végeredmény kiíratása f-string használatával
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. {dev_status}")
