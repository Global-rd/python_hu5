# Homework 05 - Object Oriented Programming
# Car Fleet Manager


# Car class
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    # Drive the car
    def drive(self, kilometers):

        if kilometers <= 0:
            print("Distance must be greater than zero.")
            return

        # Fuel consumption: 0.1% per kilometer
        fuel_needed = kilometers * 0.1

        if fuel_needed > self.fuel_level:
            print(f"Not enough fuel to drive {kilometers} km.")
            return

        self.mileage += kilometers
        self.fuel_level -= fuel_needed

        print(f"{self.brand} {self.model} drove {kilometers} km.")

    # Refuel the car
    def refuel(self, amount):

        if amount <= 0:
            print("Fuel amount must be greater than zero.")
            return

        if self.fuel_level + amount > 100:
            self.fuel_level = 100
            print(f"{self.brand} {self.model} fuel tank is now full.")

        else:
            self.fuel_level += amount
            print(f"{self.brand} {self.model} refueled by {amount}%.")

    # Display car information
    def display_info(self):

        print(f"\nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} km")
        print(f"Fuel level: {self.fuel_level:.1f}%")


# Fleet class
class Fleet:

    def __init__(self):
        self.cars = []

    # Add a car to the fleet
    def add_car(self, car):

        self.cars.append(car)
        print(f"{car.brand} {car.model} added to the fleet.")

    # Remove a car from the fleet
    def remove_car(self, car):

        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from the fleet.")

        else:
            print("Car not found in the fleet.")

    # Calculate total mileage
    def total_mileage(self):

        total = 0

        for car in self.cars:
            total += car.mileage

        return total

    # Display all cars
    def display_fleet(self):

        print("\n===== FLEET INFORMATION =====")

        if not self.cars:
            print("The fleet is empty.")
            return

        for car in self.cars:
            car.display_info()

        print("\n-----------------------------")
        print(f"Number of cars: {len(self.cars)}")
        print(f"Total fleet mileage: {self.total_mileage()} km")
        print("-----------------------------")


# Main program
def main():

    print("===== CAR FLEET MANAGER =====")

    # Create car objects
    car1 = Car("Skoda", "Fabia", 2017)
    car2 = Car("Toyota", "Corolla", 2021)
    car3 = Car("Volkswagen", "Golf", 2020)

    # Create fleet
    fleet = Fleet()

    # Add cars to fleet
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # Drive cars
    print("\n===== DRIVING =====")

    car1.drive(150)
    car2.drive(300)
    car3.drive(200)

    # Try to drive without enough fuel
    car1.drive(1000)

    # Refuel cars
    print("\n===== REFUELING =====")

    car1.refuel(20)
    car2.refuel(15)
    car3.refuel(30)

    # Drive again
    print("\n===== MORE DRIVING =====")

    car1.drive(100)
    car2.drive(50)

    # Display fleet information
    fleet.display_fleet()

    # Remove a car
    print("\n===== REMOVE CAR =====")

    fleet.remove_car(car3)

    # Display updated fleet
    fleet.display_fleet()


# Start program
if __name__ == "__main__":
    main()
