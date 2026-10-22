class Car:
    """
    Egy autót ír le: márka, modell, gyártási év, kilométeróra, üzemanyag-szint.
    """

    FUEL_PER_KM = 0.1   # class variable: kilométerenként 0.1% üzemanyag fogy
    MAX_FUEL = 100      # class variable: a tank legfeljebb 100%-ig tölthető

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0        # induló érték: 0 km
        self.fuel_level = 100   # induló érték: 100%

    def drive(self, distance: float) -> float:
        """
        Vezetés: növeli a km-óra állását, csökkenti az üzemanyagot.
        Csak annyit enged vezetni, amennyire elég az üzemanyag.
        Visszaadja a ténylegesen megtett km-t.
        """
        if distance <= 0:  # guard clause
            raise ValueError("A megtett távolságnak pozitívnak kell lennie!")

        if self.fuel_level <= 0:
            print(f"{self.brand} {self.model}: üres a tank, előbb tankolni kell!")
            return 0

        max_distance = round(self.fuel_level / Car.FUEL_PER_KM, 2)

        if distance > max_distance:
            print(f"{self.brand} {self.model}: {distance} km-re nem elég az üzemanyag, "
                  f"csak {max_distance} km-t tud megtenni.")
            distance = max_distance

        self.mileage += distance
        self.fuel_level = round(self.fuel_level - distance * Car.FUEL_PER_KM, 2)
        print(f"{self.brand} {self.model} megtett {distance} km-t.")
        return distance

    def refuel(self, amount: float) -> float:
        """
        Tankolás: növeli az üzemanyag-szintet, de legfeljebb 100%-ig.
        Visszaadja a ténylegesen betankolt mennyiséget.
        """
        if amount <= 0:
            raise ValueError("A tankolt mennyiségnek pozitívnak kell lennie!")

        space_left = Car.MAX_FUEL - self.fuel_level
        if amount > space_left:
            print(f"{self.brand} {self.model}: csak {space_left}% fér a tankba, "
                  f"ennyit tankolunk.")
            amount = space_left

        self.fuel_level = round(self.fuel_level + amount, 2)
        print(f"{self.brand} {self.model} tankolt {amount}%-ot.")
        return amount

    def __str__(self) -> str:
        return (f"{self.year} {self.brand} {self.model} | "
                f"km-óra: {self.mileage} km | üzemanyag: {self.fuel_level}%")


class Fleet:
    """
    Egy flotta, ami Car objektumokat tárol egy listában (composition).
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.cars = []

    def add_car(self, car: Car) -> None:
        # Az "in" a háttérben __eq__()-t hív. Mivel a Car nem írja felül,
        # az object.__eq__() fut le, ami az objektum azonosságát (memóriacímét)
        # nézi: két ugyanolyan márkájú és évjáratú autó is felvehető,
        # de ugyanazt az objektumot kétszer nem lehet hozzáadni.
        if car in self.cars:
            print(f"Ez az autó már a flottában van: {car.brand} {car.model}")
            return

        self.cars.append(car)
        print(f"Hozzáadva a flottához: {car.brand} {car.model}")

    def remove_car(self, car: Car) -> None:
        if car in self.cars:
            self.cars.remove(car)
            print(f"Eltávolítva a flottából: {car.brand} {car.model}")
        else:
            print(f"Ez az autó nincs a flottában: {car.brand} {car.model}")

    def get_total_mileage(self) -> float:
        total = 0
        for car in self.cars:
            total += car.mileage
        return total

    def display_cars(self) -> None:
        print(f"\n{self.name} autói:")
        if not self.cars:
            print("A flotta üres.")
            return
        for number, car in enumerate(self.cars, 1):
            print(f"{number}. {car}")


def main():
    # 1. Autók létrehozása
    car_1 = Car("Toyota", "Corolla", 2020)
    car_2 = Car("Ford", "Focus", 2018)
    car_3 = Car("Skoda", "Octavia", 2022)

    # 2. Flotta létrehozása, autók hozzáadása
    fleet = Fleet("Céges flotta")
    fleet.add_car(car_1)
    fleet.add_car(car_2)
    fleet.add_car(car_3)
    fleet.add_car(car_1)  # ugyanaz az objektum még egyszer -> nem kerül be újra

    # 3. Műveletek: vezetés, tankolás
    print("\n--- Műveletek ---")
    car_1.drive(150)
    car_1.refuel(10)
    car_2.drive(1200)     # több, mint amire elég az üzemanyag
    car_2.refuel(50)
    car_3.drive(300)
    car_3.refuel(80)      # több, mint amennyi befér

    # Hibás érték kezelése
    try:
        car_1.drive(-20)
    except ValueError as e:
        print(f"Hiba: {e}")

    # 4. Állapot és összesítés
    fleet.display_cars()
    print(f"Összes megtett km a flottában: {fleet.get_total_mileage()} km")

    # 5. Autó eltávolítása
    print()
    fleet.remove_car(car_2)
    fleet.display_cars()
    print(f"Összes megtett km a flottában: {fleet.get_total_mileage()} km")


if __name__ == "__main__":
    main()
