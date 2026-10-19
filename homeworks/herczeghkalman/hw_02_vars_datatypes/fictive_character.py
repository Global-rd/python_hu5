#változók, user Input, string metódusok, type conversation, f-string használata

"""
upper: összes betű nagybetűs, 
strip: a szöveg elejéről és végéről eltávolítja a szóközöket és a whitespace karaktereket.
"""


name = input("Your name: ").upper().strip()

#Az int tipuskonverzáció átkonvertálja az értéket egész számmá.

age = int(input("Your age in years: "))

python_experience_in_years = int(input("Your Python experience in years: "))

#A round függvény egy szám kerekítésére használható.

age_in_days = round(age * 365.25)

"""
Az f-string arra való, hogy változókat és kifejezéseket könnyen be tudjunk tenni egy szövegbe
és a kapcsos zárójelek közé írt értéket a Python behelyettesíti.
"""

print(
    f"My character is {age_in_days} days old. "
    f"His/her name is {name} "
    f"and he/she has {python_experience_in_years} years experience."
)











