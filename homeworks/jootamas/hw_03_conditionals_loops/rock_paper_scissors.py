"""
Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. A
program kérje be, hogy hány kört akarnak játszani a játékosok. Figyelj oda, hogy
olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent
játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a
körök számát amíg páratlan számot nem ad meg. Ezután a program felváltva kérje
be az első és második játékos válaszát, ami kizárólag a következő stringek
valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát
ahogy a körök számánál. Egy adott kör addig ne érjen véget, amíg valaki nem nyer
(döntetlen esetén az adott kört újra kell játszani). Tárold a nyertesek pontjait, és
minden kör végén növeld az aktuális játékos pontszámát. A végén printeld ki ki
nyert, és hány ponttal.
"""

# a lehetseges valaszok es ki gyoz le kit, a kiertekeleshez
available_options = {
  "rock" : "scissors",
  "paper" : "rock",
  "scissors" : "paper"
}

# korok szama
rounds_count = 0

# eredmenyek
rounds_results = []

# pontok
users_points = [0, 0]

# korok szamanak bekerese

print(f"Kő-papír-olló játék, lehetséges válaszok: {list(available_options.keys())}")

while True:
  rounds_count = input("Kérlek add meg hány kör legyen a játékban (egész, páratlan szám, pl. 9): ")
  if not(rounds_count.isdigit()):
    print("A megadott érték nem szám, kérlek próbáld újra!")
  elif int(rounds_count) % 2 == 0:
    print("A megadott érték nem páratlan szám!")
  else:
    break

rounds_count = int(rounds_count)

# jatek inditasa

while (round := users_points[0] + users_points[1]) < rounds_count:

  answer1 = ""
  while answer1 not in available_options:
    answer1 = input(f"{round+1}. kör, add meg az 1-es játékos válaszát: ")
    if answer1 not in available_options:
      print(f"A(z) {answer1} hibás válasz, lehetséges opciók: {list(available_options.keys())}")

  answer2 = ""
  while answer2 not in available_options:
    answer2 = input(f"{round+1}. kör, add meg az 2-es játékos válaszát: ")
    if answer2 not in available_options:
      print(f"A(z) {answer2} hibás válasz, lehetséges opciók: {list(available_options.keys())}")

  if answer1 == answer2:
    print("Ez a kör döntetlen, próbáljátok újra!")
    continue

  if available_options[answer1] == answer2:
    users_points[0] += 1
  else:
    users_points[1] += 1

print(
  f"A(z) {"1" if users_points[0] > users_points[1] else "2"}-es játékos nyert,",
  f"{users_points[0] if users_points[0] > users_points[1] else users_points[1]} ponttal"
)
