"""
Car Fleet Manager
"""

class Car:
    # Autó osztály.

    def __init__(self, brand, model, year):
        # Alapadatok beállítása
        self.brand = brand
        self.model = model
        self.year = year

        # Kezdőértékek
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, kilometers):
        # Vezetés adott kilométerrel.

        if kilometers <= 0:
            print("A távolságnak pozitívnak kell lennie.")
            return

        # 1 km = 0.1 százalékpont üzemanyag
        required_fuel = kilometers * 0.1

        if required_fuel <= self.fuel_level:
            self.mileage += kilometers
            self.fuel_level -= required_fuel

            print(
                f"{self.brand} {self.model} drove "
                f"{kilometers} km."
            )

        else:
            # Kiszámoljuk, mennyit tud még menni
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0

            print(
                f"Not enough fuel. "
                f"{self.brand} {self.model} only drove "
                f"{max_distance:.0f} km."
            )

    def refuel(self, amount):
        # Tankolás százalékban megadott mennyiséggel.

        if amount <= 0:
            print("A tankolási mennyiségnek pozitívnak kell lennie.")
            return

        self.fuel_level += amount

        # Maximum 100%
        if self.fuel_level > 100:
            self.fuel_level = 100

        print(
            f"{self.brand} {self.model} refueled. "
            f"Current fuel: {self.fuel_level:.1f}%"
        )

    def display_info(self):
        # Autó adatainak megjelenítése.

        print(
            f"{self.brand} {self.model} ({self.year}) | "
            f"Mileage: {self.mileage:.0f} km | "
            f"Fuel: {self.fuel_level:.1f}%"
        )


class Fleet:
    # Flotta osztály.

    def __init__(self):
        # Autók listája
        self.cars = []

    def add_car(self, car):
    # Autó hozzáadása.

     if car in self.cars:
        print("Ez az autó már szerepel a flottában.")
        return

     self.cars.append(car)

   
    def remove_car(self, car):
    # Autó eltávolítása.

     if car in self.cars:
        print("Ez az autó még nem szerepel a flottában.")
        return
        
     self.cars.remove(car)

    def get_total_mileage(self):
        # Flotta összes kilométere.

        total = 0

        for car in self.cars:
            total += car.mileage

        return total

    def display_fleet(self):
        # Flotta megjelenítése.

        print("\nFleet vehicles:")

        for car in self.cars:
            car.display_info()


# Autók létrehozása
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Focus", 2018)
car3 = Car("BMW", "X5", 2022)

# Flotta létrehozása
fleet = Fleet()

# Autók hozzáadása
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

# Műveletek
car1.drive(200)
car1.refuel(15)

car2.drive(500)

car3.drive(300)
car3.refuel(10)

# Autók adatainak megjelenítése
fleet.display_fleet()

# Flotta összesített adatai
print(
    f"\nTotal fleet mileage: "
    f"{fleet.get_total_mileage():.0f} km"
)