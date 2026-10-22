"""
HÁZI FELADAT 05: Autóflotta kezelés OOP alapokon
hw_05_oop/car_fleet_mgr_v1.py
"""

class InvalidAmountError(Exception):
    """Érvénytelen (nulla vagy negatív) mennyiség."""

class CarNotFoundError(Exception):
    """A keresett autó nincs a flottában."""


class CarBrand:
    """Autómárka: a márka neve és származási országa."""

    def __init__(self, brand_name: str, brand_nationality: str):
        """Létrehozza a márkát.

        brand_name: a márka neve (pl. "Renault")
        brand_nationality: a márka származási országa (pl. "French")
        """
        self.brand_name = brand_name
        self.brand_nationality = brand_nationality

    def __str__(self):
        """Szöveges alak: márkanév (nemzetiség)."""

        return f"{self.brand_name} ({self.brand_nationality})"


class CarModel:
    """Autómodell: a típus neve, márkája, évjárata és fogyasztása."""

    def __init__(self, model_name: str, car_brand: CarBrand, model_year: int, fuel_per_km: float):
        """Létrehozza a modellt.
        model_name: a modell neve (pl. "Clio")
        car_brand: a modell márkája (CarBrand objektum)
        model_year: a modell gyártási éve
        fuel_per_km: üzemanyag-fogyasztás, az üzemanyag-szint csökkenése százalékpontban kilométerenként
        """
        if fuel_per_km <= 0:
            raise InvalidAmountError("The fuel_per_km must be positive!")
                
        self.model_name  = model_name
        self.car_brand   = car_brand
        self.model_year  = model_year
        self.fuel_per_km = fuel_per_km  # üzemanyag-fogyasztás: % / km

    def __str__(self):
        """Objektum szöveges alakja: "márka modell (évjárat)"."""
        return f"{self.car_brand.brand_name} {self.model_name} ({self.model_year})"


class Car:
    """Egy konkrét autó: a modellje, rendszáma és színe mellett a saját kilométeróra-állása és üzemanyag-szintje."""

    MAX_FUEL = 100

    def __init__(self, car_model: CarModel, car_plate: str, color: str):
        """Létrehozza az autót a megadott modellből.

        A kilométeróra 0-ról, az üzemanyag-szint 100%-ról indul.
        car_model: az autó modellje (CarModel objektum)
        car_plate: az autó rendszáma (pl. "ABC-123")
        color: az autó színe (pl. "red")
        """
        self.car_model  = car_model
        self.car_plate  = car_plate
        self.color      = color
        self.mileage    = 0
        self.fuel_level = 100

    def drive(self, km: float) -> tuple[float, float, float]:
        """A megadott távolság levezetése a modell fogyasztásának figyelembe vétele szerint.

        Ha a az aktuális üzemanyag nem elégendő a kért távolságra, akkor csak a hatótávig megy.
        km: a megteendő távolság kilométerben (pozitív szám)
        Visszatérési érték: tuple (megtett km, maradék üzemanyag %, még megtehető km).
        Kivétel: InvalidAmountError, ha a km nulla vagy negatív.
        """
        if km <= 0:
            raise InvalidAmountError("The distance must be positive!")

        max_km = self.fuel_level / self.car_model.fuel_per_km
        if km > max_km:
            km = max_km

        self.mileage += km
        self.fuel_level -= km * self.car_model.fuel_per_km
        if self.fuel_level < 0:
            self.fuel_level = 0
        remaining_km = self.fuel_level / self.car_model.fuel_per_km
        return km, self.fuel_level, remaining_km

    def refuel(self, amount: float) -> float:
        """Feltölti az üzemanyag-szintet, de legfeljebb 100%-ig.

        amount: a betöltendő mennyiség százalékban (pozitív szám)
        Visszatérési érték: a ténylegesen betöltött mennyiség.
        Kivétel: InvalidAmountError, ha az amount nulla vagy negatív.
        """
        if amount <= 0:
            raise InvalidAmountError("The refuel amount must be positive!")

        free_space = Car.MAX_FUEL - self.fuel_level
        if amount > free_space:
            amount = free_space

        self.fuel_level += amount
        return amount

    def __str__(self):
        """Szöveges alak: a modell, a rendszám, a szín, a kilométeróra állása és az üzemanyag-szint."""
        return (f"{self.car_plate} {self.car_model} {self.color} \t "
                f"mileage: {self.mileage:>6.1f} km\tfuel: {self.fuel_level:>4.1f}% \tremaining range: {self.fuel_level / self.car_model.fuel_per_km:>6.1f} km")


class Fleet:
    """Autóflotta: Car objektumok listáját kezeli."""

    def __init__(self, name: str):
        """Létrehozza az üres flottát.

        name: a flotta neve
        """
        self.name = name
        self.cars = []

    def add_car(self, car: Car):
        """Hozzáadja a megadott autót a flottához.

        car: a hozzáadandó Car objektum
        """
        self.cars.append(car)

    def remove_car(self, car: Car):
        """Kiveszi a megadott autót a flottából.

        car: az eltávolítandó Car objektum
        Kivétel: CarNotFoundError, ha az autó nincs a flottában.
        """
        if car not in self.cars:
            raise CarNotFoundError(f"Car not found in the fleet: {car.car_model}")
        self.cars.remove(car)

    def total_mileage(self) -> float:
        """Visszaadja a flotta összes autójának összes megtett kilométerét."""
        total = 0
        for car in self.cars:
            total += car.mileage
        return total

    def list_cars(self):
        """Visszaadja a flotta nevét és az összes autó állapotát."""
        return {
            "fleet_name": self.name,
            "cars": [str(car) for car in self.cars]
        }


def print_fleet(fleet: Fleet):
    """Kiírja a flotta adatait áttekinthető formában."""
    print(f"\tFleet: {fleet.name} ## Cars ({len(fleet.cars)}):")
    if not fleet.cars:
        print("\t\tNo cars in the fleet.")
        return

    
    for index, car in enumerate(fleet.cars, start=1):
        remaining_range = car.fuel_level / car.car_model.fuel_per_km
        print(
            f"\t\t{index}. {car.car_plate} {car.car_model} {car.color}\tMileage: {car.mileage:>6.1f} km\tFuel: {car.fuel_level:>4.1f}%\tRemaining range: {remaining_range:>6.1f} km"
        )


def main():
    """Bemutató: márkák, modellek és autók létrehozása, vezetés, tankolás, flotta kezelése."""
    # BRAND-ek
    renault = CarBrand(brand_name="Renault", brand_nationality="French")
    fiat = CarBrand(brand_name="Fiat", brand_nationality="Italian")
    toyota = CarBrand(brand_name="Toyota", brand_nationality="Japanese")

    # CAR_MODEL-ek
    clio1 = CarModel(model_name="Clio1", car_brand=renault, model_year=2019, fuel_per_km=0.15)
    clio2 = CarModel(model_name="Clio2", car_brand=renault, model_year=2020, fuel_per_km=0.14)
    panda = CarModel(model_name="Panda", car_brand=fiat, model_year=2021, fuel_per_km=0.13)
    yaris = CarModel(model_name="Yaris", car_brand=toyota, model_year=2018, fuel_per_km=0.1)

    # CAR objektumok létrehozása
    car_1 = Car(car_plate = "ABC-135", car_model = clio1, color = "red")
    car_2 = Car(car_plate = "DEF-222", car_model = panda, color = "white")
    car_3 = Car(car_plate = "GHI-790", car_model = yaris, color = "blue")
    car_4 = Car(car_plate = "JKL-444", car_model = clio2, color = "black")

    fleet = Fleet("City Fleet")
    fleet.add_car(car_1)
    fleet.add_car(car_2)
    fleet.add_car(car_3)
    fleet.add_car(car_4)

    print("\n- Initial state: --------------------------------------------------------------------------------------------------------------------")
    print_fleet(fleet)

    print("\n- Driving: --------------------------------------------------------------------------------------------------------------------------")
    for car, km in ((car_1, 300), (car_2, 2000), (car_3, 200), (car_4, 100)):
        driven_km, fuel_left, remaining_km = car.drive(km)
        print(f"\t{car.car_plate} ({car.car_model.model_name}) \trequested: {km:>6.1f} km, \tdrove: {driven_km:>6.1f} km, "
              f"\tfuel left: {fuel_left:>6.1f}%, range left: {remaining_km:>6.1f} km")
    print("\n- Refuelling: -----------------------------------------------------------------------------------------------------------------------")
    print(f"\t{car_2.car_plate} ({car_2.car_model.model_name}) refuelled: {car_2.refuel(40):>6.1f}% ")
    print(f"\t{car_1.car_plate} ({car_1.car_model.model_name}) refuelled: {car_1.refuel(50):>6.1f}% ")
    print(f"\t{car_3.car_plate} ({car_3.car_model.model_name}) refuelled: {car_3.refuel(80):>6.1f}% ")
    
    try:
        print(f"\n\t{car_3.car_plate} ({car_3.car_model.model_name})  car_3.drive(-5) -->")
        car_3.drive(-5)
    except InvalidAmountError as e:
        print(f"\tError: {e}")

    print("\n- Re-list fleet: ---------------------------------------------------------------------------------------------------------------------")
    print_fleet(fleet)
    print(f"\nTotal mileage of the fleet: {fleet.total_mileage():.1f} km")

    print("\n- Remove cars: -----------------------------------------------------------------------------------------------------------------------")
    for car_to_remove in (car_3, car_3):  # másodszor már nincs a flottában
        try:
            fleet.remove_car(car_to_remove)
            print(f"Car removed from the fleet: {car_to_remove}")
        except CarNotFoundError as e:
            print(f"Error: {e}")
    print("\n- Re-list fleet: ---------------------------------------------------------------------------------------------------------------------")
    print_fleet(fleet)
    print(f"\nTotal mileage after removal: {fleet.total_mileage():.1f} km")


if __name__ == "__main__":
    main()
