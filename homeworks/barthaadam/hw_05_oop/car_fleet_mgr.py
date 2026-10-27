class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        max_distance = self.fuel_level / 0.1
        actual_distance = min(distance, max_distance)
        self.mileage += actual_distance
        self.fuel_level = max(0, self.fuel_level - actual_distance * 0.1)
        return actual_distance

    def refuel(self, amount):
        if amount < 0:
            raise ValueError("Fuel amount cannot be negative.")

        self.fuel_level = min(100, self.fuel_level + amount)

    def __str__(self):
        return (
            f"{self.brand} {self.model} ({self.year}) | "
            f"Mileage: {self.mileage:.1f} km | "
            f"Fuel: {self.fuel_level:.1f}%"
        )


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError("Only Car objects can be added.")
        if car not in self.cars:
            self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def display_cars(self):
        if not self.cars:
            print("The fleet is empty.")
        for car in self.cars:
            print(car)


def main():
    fleet = Fleet()
    volvo = Car("Volvo", "XC40", 2018)
    toyota = Car("Toyota", "Corolla", 2020)
    ford = Car("Ford", "Focus", 2017)

    fleet.add_car(volvo)
    fleet.add_car(toyota)
    fleet.add_car(ford)

    volvo.drive(200)
    actual_distance = toyota.drive(1200)
    print(f"Toyota actually travelled: {actual_distance:.1f} km")
    ford.drive(150)
    toyota.refuel(30)
    volvo.refuel(50)

    print("\nFleet status:")
    fleet.display_cars()
    print(f"Total mileage: {fleet.total_mileage():.1f} km")

    fleet.remove_car(ford)
    print("\nAfter removing the Ford:")
    fleet.display_cars()
    print(f"Total mileage: {fleet.total_mileage():.1f} km")


if __name__ == "__main__":
    main()
