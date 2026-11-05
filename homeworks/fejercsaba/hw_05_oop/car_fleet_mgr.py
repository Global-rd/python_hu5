"""
Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
Márka (brand), Modell (model), Gyártási év (year), 
Kilométeróra állása (mileage), induló értéke 0., Üzemanyag-szint 
 Fleet osztályt, amely kezeli a Car objektumokat: 
● Az osztály rendelkezzen egy listával, amelyben az autók találhatóak. 
● Tartalmazzon metódusokat Car objektumok hozzáadására és 
eltávolítására a flottába/flottából. 
● Tartalmazzon egy metódust, amely összesíti a flotta összes autójának 
összes kilométerét.  
● Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts 
végre néhány műveletet (vezetés, tankolás),  jelenítsd meg az autók 
állapotát és a flotta összesítő adatait. 
"""


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mile age: {self.mileage:.1f} km")
        print(f"Fuel level: {self.fuel_level:.1f}%")

    
    def drive(self, km):
        if km < 0:
            print("\nThe refueling amount cannot be negative!!!")
            return

        # Ennyi kilométer tehető meg a rendelkezésre álló üzemanyaggal
        max_km = 10 * self.fuel_level 

        # Csak annyit vezethetünk amennyit lehet
        actual_km = min(km, max_km)

        self.mileage += actual_km
        self.fuel_level -= actual_km * 0.1

        # Kerekítési hibák elkerülése
        self.fuel_level = max(0.0, round(self.fuel_level, 2))

        print(f"{self.brand} {self.model}: "
              f"{actual_km:.1f} km completed.")

        if actual_km < km:
            print(f"The road ({actual_km:.1f}) cannot be negative!")


    def refuel(self, amount):
        if amount < 0:
            print("The refueling amount cannot be negative!!!!!")
            return

        # Az üzemanyagszint legfeljebb 100% lehet
        old_level = self.fuel_level
        self.fuel_level = min(100.0, self.fuel_level + amount)

        added = self.fuel_level - old_level

        print(f"{self.brand} {self.model}: "
              f"{added:.1f}% fuel added.")


class Fleet:
    def __init__(self):
        self.cars = []

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def add_car(self, car):
        if car not in self.cars:
            self.cars.append(car)
            print(f"{car.brand} {car.model} ({car.year}) added to the fleet")
        else:
            print("This car is already in the fleet.")
    
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} ({car.year}) removed from the fleet")
        else:
            print(f"The {car.brand} {car.model} ({car.year}) is not found in the fleet.")

    def display_fleet(self):
        print("\n  ---------- The FLEET consists of these CARS ---------- ")

        for car in self.cars:
            car.display_info()

        print(f"NUMBER OF CARS: {len(self.cars)}")
        print(f"TOTAL KILOMETERS DONE: "
              f"{self.total_mileage():.1f} km")
        print("\n  ------------------------------------------------------- ")

# autó objektum létrehozás
car1 = Car("Suzuki", "Swift", 2002)
car2 = Car("Ford", "Focus", 2025)
car3 = Car("Opel", "Corsa", 2021)
car4 = Car("Tesla", "Roadster", 2026)
car5 = Car("Volvo", "EX60", 2026)

#flotta objektum létrehozás
fleet = Fleet()

# Autók hozzáadása a flottához
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)
fleet.add_car(car5)

# Az autók és a flotta kezdeti adatainak megjelenítése
print("\nINITIAL FLEET STATUS")
fleet.display_fleet()

print("\nDRIVE ")
car1.drive(250)
car2.drive(300)
car3.drive(1500)  # Nem lesz elegendő üzemanyag
car4.drive(-10)
car5.drive(650)

# kiveszem a car4-et a flottából
fleet.remove_car(car4)


print("\n Fuel intake ")
car1.refuel(50)
car3.refuel(100)   # Legfeljebb 100%-ig tölthető
car5.refuel(300) 

print("\nDRIVE")
car1.drive(180)
car3.drive(200)
car5.drive(150)

# Az autók és a flotta adatainak megjelenítése
fleet.display_fleet()
