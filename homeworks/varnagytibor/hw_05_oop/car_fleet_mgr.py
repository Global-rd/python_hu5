#5. házi feladat - autóflotta-kezelő (Car és Fleet osztály)

FUEL_PER_KM = 0.1   #ennyi % üzemanyag fogy kilométerenként
MAX_FUEL = 100      #a tank 100%-nál jobban nem tölthető


class Car:
    """Egy autó: márka, modell, gyártási év, km-óra állás és üzemanyag-szint."""

    def __init__(self, brand, model, year, mileage=0, fuel_level=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage        #km-óra állása, induló értéke 0
        self.fuel_level = fuel_level  #üzemanyag-szint %-ban, induló értéke 100

    def drive(self, km):
        """Megtesz adott számú km-t, de csak annyit, amennyire elég az üzemanyag.

        Visszaadja a ténylegesen megtett kilométert.
        """
        if km <= 0:
            print(f"{self.brand} {self.model}: the distance must be positive.")
            return 0

        #ennyi km-re elég a tankban lévő üzemanyag
        max_km = self.fuel_level / FUEL_PER_KM
        driven_km = min(km, max_km)

        if driven_km < km:
            print(f"{self.brand} {self.model}: not enough fuel for {km} km, "
                  f"driving only {driven_km:.1f} km.")

        self.mileage += driven_km
        self.fuel_level -= driven_km * FUEL_PER_KM
        #lebegőpontos kerekítési hiba ellen: ne legyen pl. -0.0000001%
        self.fuel_level = max(round(self.fuel_level, 2), 0)
        return driven_km

    def refuel(self, amount):
        """Feltölti a tankot adott mennyiséggel (%), legfeljebb 100%-ig.

        Visszaadja a ténylegesen betöltött mennyiséget.
        """
        if amount <= 0:
            print(f"{self.brand} {self.model}: the refuel amount must be positive.")
            return 0

        added = min(amount, MAX_FUEL - self.fuel_level)
        if added < amount:
            print(f"{self.brand} {self.model}: the tank is full, "
                  f"only {added:.1f}% could be added.")

        self.fuel_level += added
        return added

    def __str__(self):
        return (f"{self.year} {self.brand} {self.model} - "
                f"mileage: {self.mileage:.1f} km, fuel: {self.fuel_level:.1f}%")


class Fleet:
    """Autóflotta: a Car objektumokat egy listában tárolja."""

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        """Hozzáad egy autót a flottához (ugyanazt az autót kétszer nem)."""
        if car in self.cars:
            print(f"{car.brand} {car.model} is already in the fleet.")
            return
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to the fleet.")

    def remove_car(self, car):
        """Eltávolít egy autót a flottából, ha benne van."""
        if car not in self.cars:
            print(f"{car.brand} {car.model} is not in the fleet.")
            return
        self.cars.remove(car)
        print(f"{car.brand} {car.model} removed from the fleet.")

    def total_mileage(self):
        """Összesíti a flotta összes autójának kilométerét."""
        return sum(car.mileage for car in self.cars)

    def show_status(self):
        """Kiírja az autók állapotát és a flotta összesítő adatait."""
        print("\n--- Fleet status ---")
        if not self.cars:
            print("The fleet is empty.")
        for number, car in enumerate(self.cars, start=1):
            print(f"{number}. {car}")
        print(f"Cars in the fleet: {len(self.cars)}")
        print(f"Total mileage of the fleet: {self.total_mileage():.1f} km\n")


if __name__ == "__main__":
    #néhány autó létrehozása
    car1 = Car("Toyota", "Corolla", 2019)
    car2 = Car("Skoda", "Octavia", 2021)
    car3 = Car("Ford", "Focus", 2017)

    #flotta összeállítása
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    fleet.add_car(car1)  #már benne van - nem kerül be még egyszer
    fleet.show_status()

    #vezetés
    car1.drive(250)    #25% fogy
    car2.drive(400)    #40% fogy
    car3.drive(1200)   #csak 1000 km-re elég a 100% üzemanyag
    car2.drive(-10)    #érvénytelen távolság
    fleet.show_status()

    #tankolás
    car1.refuel(10)    #75% -> 85%
    car2.refuel(70)    #60% -> csak 100%-ig tölthető
    car3.refuel(50)    #0% -> 50%
    fleet.show_status()

    #még egy kör vezetés, majd egy autó eltávolítása
    car3.drive(300)
    fleet.remove_car(car2)
    fleet.remove_car(car2)  #már nincs benne
    fleet.show_status()
