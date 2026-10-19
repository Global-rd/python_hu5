# Bekérjük a karakter nevét.
character_name = input("Character name: ").strip().upper()
# Bekérjük az életkort, majd egész számmá alakítjuk.
age_in_years = int(input("Character age: "))
# Kiszámítjuk a karakter életkorát napokban.
age_in_days = age_in_years * 365
# Bekérjük a Python-tapasztalatot években.
python_experience = float(input("Python experience in years: "))
# Megkérdezzük, hogy szeretne-e Python-fejlesztő lenni.
developer_answer = input("Does the character want to be a Python developer? (yes/no): ").strip().lower()
developer_message = "wants" if developer_answer == "yes" else "does not want"
# Egy mondatban kiírjuk a karakter adatait.
print(
    f"My character is {age_in_days} days old. "
    f"His/her name is {character_name} and he/she has "
    f"{python_experience} years experience. "
    f"He/she {developer_message} to be a professional developer."
)

