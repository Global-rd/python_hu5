
# Kérj be a felhasználótól adatokat, majd írasd ki őket egy mondatban.
name= input("Mi a neved? "). strip().upper()
age = int(input("Hány éves vagy? "))
experience = int(input("Hány év tapasztalatod van Python programozásban? "))

#Extra, nem kötelező feladat, kérj be egy igen/nem választ, majd rakd hozzá a mondathoz.
profi = input("Szeretnél profi Python programozóvá válni? (yes/no) ").strip().lower()

#El kell tárolni a választ és kiértékelni
status = "wants" if profi == "yes" else "does not want"

#Kiíratás, az extra feladat valamiért nem íratódik ki, ha egy printbe teszem, nem értem miért nem :(
print(f"My character is {age} old. His/her name is {name} and he/she has {experience}" ""\
      f"years experience. He/she {status} to be a Python developer.")
