class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, kilometers):
        if kilometers < 0:
            raise ValueError("Kilometers cannot be negative.")

        max_distance = self.fuel_level / 0.1

        if kilometers > max_distance:
            kilometers = max_distance
            print(
                f"{self.brand} {self.model}: Not enough fuel. "
                f"Drove only {kilometers:.1f} km."
            )

        self.mileage += kilometers
        self.fuel_level -= kilometers * 0.1

        if self.fuel_level < 0:
            self.fuel_level = 0

    def refuel(self, amount):
        if amount < 0:
            raise ValueError("Fuel amount cannot be negative.")

        self.fuel_level += amount

        if self.fuel_level > 100:
            self.fuel_level = 100

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
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def show_fleet(self):
        print("\nFleet Status:")
        for car in self.cars:
            print(car)

        print(f"\nTotal fleet mileage: {self.total_mileage():.1f} km")


# Create cars
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Focus", 2018)
car3 = Car("Tesla", "Model 3", 2023)

# Create fleet
fleet = Fleet()

# Add cars to fleet
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

# Perform operations
car1.drive(150)
car2.drive(300)
car3.drive(1200)  # More than fuel allows

car1.refuel(20)
car2.refuel(15)

# Display car states and fleet summary
fleet.show_fleet()

# Remove a car
fleet.remove_car(car2)

print("\nAfter removing one car:")
fleet.show_fleet()