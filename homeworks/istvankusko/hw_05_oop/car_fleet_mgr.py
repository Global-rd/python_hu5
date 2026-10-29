# car_fleet


class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0.0
        self.fuel_level = 100.0  # In percentage (0.0 - 100.0)

    def drive(self, distance: float):
        """
        Drive a given distance.
        If there is not enough fuel, the car only drives the maximum possible distance.
        1 km = 0.1% fuel consumption.
        """
        if distance <= 0:
            print("The distance to travel must be positive.")
            return

        # Maximum distance that can be covered with the current fuel level
        max_distance = self.fuel_level / 0.1

# Question
    # Could this be done more beautifully, better, or more efficiently?

        if distance <= max_distance:
            driven = distance
            self.mileage += driven
            self.fuel_level -= driven * 0.1
            print(f"[{self.brand} {self.model}] Successfully drove {driven:.1f} km. Current mileage: {self.mileage:.1f} km, Fuel: {self.fuel_level:.1f}%.")
        else:
            driven = max_distance
            self.mileage += driven
            self.fuel_level = 0.0
            print(f"[{self.brand} {self.model}] Out of fuel! Managed to drive only {driven:.1f} km out of the requested {distance:.1f} km. Current mileage: {self.mileage:.1f} km, Fuel: 0.0%.")
# ---------

    def refuel(self, amount: float):
        """
        Refuel by a given amount of fuel (in percentage points).
        The fuel level cannot exceed 100%.
        """
        if amount <= 0:
            print("The refuel amount must be positive.")
            return

        if self.fuel_level + amount > 100.0:
            added = 100.0 - self.fuel_level
            self.fuel_level = 100.0
            print(f"[{self.brand} {self.model}] Tank is full! Added: {added:.1f}%. Current fuel: {self.fuel_level:.1f}%.")
        else:
            self.fuel_level += amount
            print(f"[{self.brand} {self.model}] Refueled: {amount:.1f}%. Current fuel: {self.fuel_level:.1f}%.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage:.1f} km, Fuel: {self.fuel_level:.1f}%"


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        """Add a car to the fleet."""
        self.cars.append(car)
        print(f"Car added to fleet: {car.brand} {car.model}")

    def remove_car(self, car: Car):
        """Remove a car from the fleet."""
        if car in self.cars:
            self.cars.remove(car)
            print(f"Car removed from fleet: {car.brand} {car.model}")
        else:
            print(f"Car ({car.brand} {car.model}) is not found in the fleet.")

    def get_total_mileage(self) -> float:
        """Total mileage of all cars in the fleet."""
        return sum(car.mileage for car in self.cars)

    def display_fleet_status(self):
        """Displays the current status of the fleet."""
        print("\n=== FLEET STATUS ===================")
        if not self.cars:
            print("The fleet is currently empty.")
            return
        for idx, car in enumerate(self.cars, start=1):
            print(f"{idx}. {car}")
        print(f"Total fleet mileage: {self.get_total_mileage():.1f} km")
        print("======================================\n")


# ---------------------------------------------------------
# Testing 

if __name__ == "__main__":
    fleet = Fleet()

    car1 = Car("Toyota", "RAV4", 2020)
    car2 = Car("Ford", "Focus", 2018)
    car3 = Car("BMW", "320i", 2022)

    print("--- Adding cars to the fleet ---")
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    fleet.display_fleet_status()

    print("--- Executing operations ---")
    car1.drive(300)   # 30% fuel consumed, 70% remaining
    car2.drive(600)   # 60% fuel consumed, 40% remaining
    car3.drive(1200)  # Can only drive 1000 km, tank runs empty (0%)

    fleet.display_fleet_status()

    print("--- Refueling and further driving ---")
    car3.refuel(50)   # Refuel to 50%
    car3.drive(200)   # Drive another 200 km
    car1.refuel(50)   # Fills up to 100%

    fleet.display_fleet_status()

    print("--- Removing a car ---")
    fleet.remove_car(car2)

    fleet.display_fleet_status()