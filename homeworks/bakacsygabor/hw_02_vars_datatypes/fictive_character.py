"""Képzeletbeli karakter létrehozása a megadott adatokból."""


# Az input() mindig szöveget ad vissza.
# A strip() levágja a szóközöket, az upper() pedig nagybetűssé teszi a nevet.
character_name = input("Character name: ").strip().upper()

# Az int() egész számmá alakítja az életkort.
age_in_years = int(input("Character age in years: "))

# Az életkort átváltjuk napokra. A szökőéveket most nem számoljuk.
age_in_days = age_in_years * 365

# A float() tört számot is elfogad, például 1.5 év tapasztalatot.
python_experience_in_years = float(
    input("Python experience in years: ")
)

# A lower() miatt a YES és a Yes válasz is megfelelő lesz.
wants_to_be_python_developer = input(
    "Should the character be a professional Python developer? (yes/no): "
).strip().lower()

# A ternary operátor kiválasztja a válaszhoz tartozó mondatot.
developer_message = (
    "He/she wants to be a Python developer!"
    if wants_to_be_python_developer == "yes"
    else "He/she does not want to be a Python developer!"
)

# A :g miatt a 2.0 helyett 2 jelenik meg, de az 1.5 megmarad.
print(
    f"My character is {age_in_days} old. "
    f"His/her name is {character_name} and he/she has "
    f"{python_experience_in_years:g} years experience. "
    f"{developer_message}"
)
