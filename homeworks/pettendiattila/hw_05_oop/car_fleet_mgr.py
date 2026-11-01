
class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0

    def drive(self, km: float):
        """
        1 km megtételéhez 0.1% üzemanyag fogy.
        """

        # Negatív távolság ellenőrzése
        if km < 0:
            print("Hiba: A távolság nem lehet negatív!")
            return

        # Szükséges üzemanyag kiszámítása
        required_fuel = km * 0.1

        if required_fuel <= self.fuel_level:
            self.mileage += km
            self.fuel_level -= required_fuel

            print(
                f"Sikeres utazás: {km} km. "
                f"Kilométeróra: {self.mileage} km, "
                f"üzemanyag: {self.fuel_level:.1f}%."
            )
        else:
            # Maximum megtehető távolság
            max_km = self.fuel_level / 0.1

            self.mileage += max_km
            self.fuel_level = 0.0

            print(
                f"Nincs elég üzemanyag! "
                f"Az autó {max_km:.1f} km-t tett meg, "
                f"és kifogyott az üzemanyag."
            )

    def refuel(self, amount: float):
        """Tankolás, maximum 100%-ig."""

        if amount <= 0:
            print("Hiba: A tankolandó mennyiségnek pozitívnak kell lennie!")
            return

        self.fuel_level += amount

        if self.fuel_level > 100:
            self.fuel_level = 100.0
            print("A tank tele lett (100%).")
        else:
            print(
                f"Sikeres tankolás. "
                f"Üzemanyag-szint: {self.fuel_level:.1f}%."
            )



class Fleet:
    def __init__(self):
        # A flotta egy üres listával indul, amiben majd a Car objektumokat tároljuk
        self.cars = []

    def add_car(self, car: Car):
        """Autó hozzáadása a flottához."""
        if car not in self.cars:
            self.cars.append(car)
            print(f"Hozzáadva a flottához: {car.brand} {car.model}")
        else:
            print("Hiba: Ez az autó már szerepel a flottában.")

    def remove_car(self, car: Car):
        """Autó eltávolítása a flottából."""
        if car in self.cars:
            self.cars.remove(car)
            print(f"Eltávolítva a flottából: {car.brand} {car.model}")
        else:
            print("Hiba: Ez az autó nem található a flottában.")

    def get_total_mileage(self) -> float:
        """
        Összesíti a flotta összes autójának összes kilométerét.
        Végigloopolunk a listán, és összeadjuk az egyes autók 'mileage' értékét.
        """
        total = 0.0
        for car in self.cars:
            total += car.mileage
        return total

#Teszt

 
# Autok letrehozasa
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("BMW", "320d", 2019)
car3 = Car("Ford", "Focus", 2022)

# Flotta letrehozasa
fleet = Fleet()

# Autok hozzaadasa
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

# Vezetes
print("\n--- Utazasok ---")
car1.drive(200)
car2.drive(350)
car3.drive(1500)

# Tankolas
print("\n--- Tankolas ---")
car1.refuel(20)
car3.refuel(50)

# Autok allapotanak megjelenitese
print("\n--- Autok allapota ---")

for car in fleet.cars:
    print(f"Marka: {car.brand}")
    print(f"Modell: {car.model}")
    print(f"Evjarat: {car.year}")
    print(f"Kilometerora: {car.mileage:.1f} km")
    print(f"Uzemanyag: {car.fuel_level:.1f}%")
    print("-------------------")

# Flotta osszesitett kilometer
print(
    f"Flotta osszes kilometer: "
    f"{fleet.get_total_mileage():.1f} km")
   