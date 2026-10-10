#kérjük be a karakter nevét
charachter_name = input("Character name: ").strip().upper()
#kérjük be a karakter életkorát, majd egész számmá alakítjuk
age_in_years = int(input("Character age: "))
#kiszámítjuk a karakter életkorát napokban
age_in_days = age_in_years * 365
#kérjük be a Python-tapasztalatot években
python_experience = float(input("Python experience in years: "))
#megkérdezzük, hogy szeretne-e Python-fejlesztő lenni
developer_answer = input("Does the character want to be a Python developer? (yes/no): ").strip().lower()
developer_message = "wants" if developer_answer == "yes" else "does not want"
#egy mondatban kiírjuk a karakter adatait
print(
    f"My character is {age_in_days} days old. "
    f"His/her name is {charachter_name} and he/she has "
    f"{python_experience} years experience. "
    f"He/she {developer_message} to be a Python developer!"
)
