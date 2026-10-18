class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        if distance <= 0:
            print("Distance must be positive.")
            return

        fuel_needed = distance * 0.1

        if fuel_needed > self.fuel_level:
            max_distance = self.fuel_level / 0.1
            print(
                f"Not enough fuel. "
                f"Maximum possible distance: {max_distance} km."
            )
            return

        self.mileage += distance
        self.fuel_level -= fuel_needed

        print(
            f"{self.brand} {self.model} drove {distance} km."
        )

    def refuel(self, amount):
        if amount <= 0:
            print("Refuel amount must be positive.")
            return

        available_capacity = 100 - self.fuel_level

        if amount > available_capacity:
            print(
                f"You can refuel maximum {available_capacity}%."
            )
            return

        self.fuel_level += amount

        print(
            f"Refueled {amount}%. "
            f"Current fuel level: {self.fuel_level}%."
        )


class Fleet:

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if not isinstance(car, Car):
            print("Only Car objects can be added to the fleet.")
            return

        self.cars.append(car)

    def remove_car(self, car):
        if car not in self.cars:
            print("Car not found in fleet.")
            return

        self.cars.remove(car)

    def get_total_mileage(self):
        total = 0

        for car in self.cars:
            total += car.mileage

        return total


car_1 = Car("Toyota", "Corolla", 2020)
car_2 = Car("Ford", "Focus", 2019)
car_3 = Car("Suzuki", "Swift", 2022)

fleet = Fleet()

fleet.add_car(car_1)
fleet.add_car(car_2)
fleet.add_car(car_3)

car_1.drive(100)
car_1.refuel(5)

car_2.drive(200)

car_3.drive(50)
car_3.refuel(3)

print(
    car_1.brand,
    car_1.model,
    car_1.year,
    car_1.mileage,
    car_1.fuel_level
)

print(
    car_2.brand,
    car_2.model,
    car_2.year,
    car_2.mileage,
    car_2.fuel_level
)

print(
    car_3.brand,
    car_3.model,
    car_3.year,
    car_3.mileage,
    car_3.fuel_level
)

print(
    "Total fleet mileage:",
    fleet.get_total_mileage()
)
