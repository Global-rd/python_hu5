#real life example: egy gépezet ami játékokat gyárt

#van egy kezelőfelülete, amin be tudjuk állítani a következőket:
#- játék típusa (pl: barbie, matchbox)
#- játék színe (sárga, kék stb.)
#ezután legyártja a játékot

#class: maga a gépezet, ami tudja hogyan kell megcsinálni az adott paraméterek alapján a játékot, van egy hozzá egy leírása
#__init__(): a gép kezelőfelülete, amivel interaktálunk amikor létre akarjuk hozni a játékot, itt egy gombnyomás hoz létre egy új játékot
#instance(példány): az osztály egy példánya, vagyis a gép által létrehozott játék (1 darab aktuális játék)
#instance method: az a cselekmény amit a játék tud csinálni, vagy amit a játékkal lehet csinálni (metódus)
#instance variable: attribútum, vagyis a tulajdonság ami jellemzi a gép által létrehozott játékot (pl: sárga szín, barbie típus)
#class variable: egy olyan változó ami kizárólag a gépet jellemzi, és nem a példányt (pl: hány játékot gyártott le eddig)
#class method: egy olyan metódus ami az osztály változóit használja/módosítja, pl: egy get_toy_count() metódus
#static method: nincs hozzáférése sem az osztályhoz, sem a példányhoz, de logikailag köthető hozzájuk. pl: használhatja e a gyerek x éves korban a játékot? ()



class Toy:

    toy_count = 0 #class variable

    def __init__(self, t_type, t_color):
        self.toy_type = t_type
        self.toy_color = t_color
        Toy.toy_count += 1

    def play(self): #instance method
        print(f"Currently playing with {self.toy_color} {self.toy_type}")

    def move(self, distance, direction):
        print(f"{self.toy_color} {self.toy_type} moved {distance} meters to the {direction}")

    @classmethod
    def get_toy_count(cls):
        return cls.toy_count

    @staticmethod
    def is_toy_safe_for_age(toy_type, age):
        if toy_type ==  "matchbox" and age < 3:
            return False
        return True


print("toy count: ", Toy.toy_count)
toy_matchbox = Toy(t_type="matchbox", t_color="yellow")
print("toy count: ", Toy.toy_count)
print(toy_matchbox)
print(toy_matchbox.toy_type)
print(toy_matchbox.toy_color)
toy_matchbox.play()

toy_barbie = Toy(t_type="barbie", t_color="pink")
print("toy count: ", Toy.toy_count)
print(toy_barbie.toy_type)
print(toy_barbie.toy_color)
toy_barbie.play()

toy_barbie_color = input("What should be the color of the barbie?")
toy_barbie.toy_color = toy_barbie_color
toy_barbie.play()

toy_matchbox.move(100, "left")

toy_count = Toy.get_toy_count()
print(toy_count)

print(Toy.is_toy_safe_for_age(toy_matchbox.toy_type, 3))

print(type(toy_matchbox))
print(isinstance(toy_matchbox, Toy))
print(isinstance("appletree", str))


