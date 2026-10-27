
class Car:
    """Egy autót reprezentáló osztály."""

    FUEL_CONSUMPTION_PER_KM = 0.1  # százalékpont / km

    def __init__(self, brand, model, year, mileage=0, fuel_level=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = max(0, mileage)
        self.fuel_level = min(100.0, max(0.0, float(fuel_level)))

    def drive(self, km):
        """Vezetés a megadott távolságon, a rendelkezésre álló üzemanyagig.

        Visszatérési érték: a ténylegesen megtett kilométer.
        """
        if not isinstance(km, (int, float)) or isinstance(km, bool):
            raise TypeError("A megtett távolságnak számnak kell lennie.")
        if km < 0:
            raise ValueError("A megtett távolság nem lehet negatív.")

        max_distance = self.fuel_level / self.FUEL_CONSUMPTION_PER_KM
        actual_distance = min(float(km), max_distance)
        fuel_used = actual_distance * self.FUEL_CONSUMPTION_PER_KM

        self.mileage += actual_distance
        self.fuel_level = max(0.0, self.fuel_level - fuel_used)
        return actual_distance

    def refuel(self, amount):
        """Üzemanyag hozzáadása; a szint nem haladhatja meg a 100%-ot.

        Visszatérési érték: a ténylegesen hozzáadott üzemanyag százalékpontban.
        """
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("A tankolt mennyiségnek számnak kell lennie.")
        if amount < 0:
            raise ValueError("A tankolt mennyiség nem lehet negatív.")

        old_level = self.fuel_level
        self.fuel_level = min(100.0, self.fuel_level + amount)
        return self.fuel_level - old_level

    def __str__(self):
        return (
            f"{self.brand} {self.model} ({self.year}) | "
            f"Kilométeróra: {self.mileage:.1f} km | "
            f"Üzemanyag: {self.fuel_level:.1f}%"
        )


class Fleet:
    """Autókat nyilvántartó flotta."""

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        """Autó hozzáadása a flottához."""
        if not isinstance(car, Car):
            raise TypeError("A flottához csak Car objektum adható.")
        if car not in self.cars:
            self.cars.append(car)

    def remove_car(self, car):
        """Autó eltávolítása; True, ha sikerült, különben False."""
        if car in self.cars:
            self.cars.remove(car)
            return True
        return False

    def total_mileage(self):
        """A flottában szereplő autók kilométeróra-állásának összege."""
        return sum(car.mileage for car in self.cars)

    def __len__(self):
        return len(self.cars)

    def show_status(self):
        """A flotta autóinak és összesítő adatainak megjelenítése."""
        print("\n--- Flotta állapota ---")
        if not self.cars:
            print("A flotta jelenleg üres.")
        else:
            for index, car in enumerate(self.cars, start=1):
                print(f"{index}. {car}")

        print(f"Autók száma: {len(self.cars)}")
        print(f"Összes megtett kilométer: {self.total_mileage():.1f} km")


def main():
    # Autók létrehozása és hozzáadása a flottához.
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Ford", "Focus", 2018)
    car3 = Car("Volkswagen", "Passat", 2016)

    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # Vezetés és tankolás.
    car1.drive(250)
    car2.drive(400)
    car2.refuel(30)
    car2.drive(150)
    car3.drive(1200)  # Csak a rendelkezésre álló üzemanyaggal tud menni.

    # Állapot és összesítő adatok.
    fleet.show_status()

    # Példa eltávolításra:
    # fleet.remove_car(car2)


if __name__ == "__main__":
    main()
