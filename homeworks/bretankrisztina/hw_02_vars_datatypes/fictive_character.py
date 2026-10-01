
# Kérj be a felhasználótól adatokat, majd írasd ki őket egy mondatban.
nev= input("Mi a neved? "). strip().upper()
eletkor = int(input("Hány éves vagy? "))
tapasztalat = int(input("Hány év tapasztalatod van Python programozásban? "))

#Extra, nem kötelező feladat, kérj be egy igen/nem választ, majd rakd hozzá a mondathoz.
profi = input("Szeretnél profi Python programozóvá válni? (yes/no) ").strip().lower()

#El kell tárolni a választ és kiértékelni
status = "wants" if profi == "yes" else "does not want"

#Kiíratás, az extra feladat valamiért nem íratódik ki, ha egy printbe teszem, nem értem miért nem :(
print(f"My character is {eletkor} old. His/her name is {nev} and he/she has {tapasztalat}" "" \
" years experience." )
print(f"He/she {status} to be a Python developer.")
