# Our Family's Car Fleet


# ezt órán vettük, nem biztos, hogy ide kell
class InvalidAmountError(Exception):
    pass


class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, km: float) -> None:
        if km <= 0:
            raise InvalidAmountError("Distance must be positive!")

        # mennyire elég a benzin?
        max_km = self.fuel_level * 10

        if km > max_km:
            km = max_km  # csak amennyire elég

        self.mileage += km
        self.fuel_level -= km * 0.1

    def refuel(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("Refuel amount must be positive!")

        self.fuel_level += amount

        if self.fuel_level > 100:
            self.fuel_level = 100  # max. 100%

    def __str__(self):
        # autó adatainak kiírása
        return (f"{self.brand} {self.model} ({self.year}) - "
                f"{self.mileage} km, fuel: {self.fuel_level}%")


class Fleet:
    def __init__(self) -> None:
        self.cars = []  # az uatók listája

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def remove_car(self, car: Car) -> None:
            # megkeressük a listában
        for fleet_car in self.cars:
            if fleet_car == car:
                self.cars.remove(fleet_car)
                return  # megvan

    def get_total_mileage(self) -> float:
        total = 0

        # km-ek összeadása
        for car in self.cars:
            total += car.mileage

        return total

    def show_fleet(self) -> None:
        print("--- Fleet status ---")

        for car in self.cars:
            print(car)

        print(f"Number of cars: {len(self.cars)}")
        print(f"Total mileage: {self.get_total_mileage()} km")
        print()


def main():
    car_1 = Car("Opel", "Corsa", 2019)
    car_2 = Car("Seat", "Leon", 2020)
    car_3 = Car("BMW", "116i", 2018)
    car_4 = Car("Citroen", "C3", 2021)

    fleet = Fleet()

    fleet.add_car(car_1)
    fleet.add_car(car_2)
    fleet.add_car(car_3)
    fleet.add_car(car_4)

    # ez az induló állapot
    fleet.show_fleet()

    car_1.drive(250)
    car_2.drive(400)
    car_3.drive(1200)  # csak 1000 km-re elég
    car_4.drive(180)

    car_2.refuel(30)
    car_3.refuel(150)  # max 100%
    car_4.refuel(15)

    # ezt is vettük órán, lehet, hogy itt nem szükséges
    try:
        car_1.drive(-50)
    except InvalidAmountError as error:
        print(f"Error: {error}")

    print()

    # állapot a műveletek után
    fleet.show_fleet()

    fleet.remove_car(car_2)

    # állapot az autó törlése után
    fleet.show_fleet()


if __name__ == "__main__":
    main()
