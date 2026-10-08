#mire jók a functionök?
#kód újrahasznosítása
#rendezettség fokozása

#separation of concerns: különbözö feladatok / feladatrészek function-ökre bontása
#szabályok:
#DRY: DON'T REPEAT YOURSELF! -> repetitív logika absztrakciója function-ökkel
#Single Responsibility principle: -> egy function egy feladatért legyen felelős
# kerüljük a mutable object-eket default argumentekként!

#bad example

name_1 = "Alice"
name_2 = "Bob"
name_3 = "Dexter"

print(f"Hello {name_1}, welcome home!")
print(f"Hello {name_2}, welcome home!")
print(f"Hello {name_3}, welcome home!")

#good example:
print("----------------")

def greet_user(name):
    print(f"Hello {name}, welcome on board!")

greet_user(name_1)
greet_user(name_2)
greet_user(name_3)

names = ["Alice", "Bob", "Dexter"]

for name in names:
    greet_user(name)




