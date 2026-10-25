
# Homework 5 - Object-Oriented Programming
# Car Fleet Manager - Simon David


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    # Driving the car and calculating fuel consumption
    def drive(self, distance):
        if distance <= 0:
            print("Distance must be greater than zero.")
            return

        remaining_distance = distance

        while remaining_distance > 0:
            max_distance = self.fuel_level / 0.1

            if remaining_distance > max_distance:
                print("\nWARNING: Not enough fuel!")
                print("You will need to refuel during the travel.")
                print(f"Available range: {max_distance:.1f} km")
                print(f"Remaining distance: {remaining_distance:.1f} km")

                while True:
                    choice = input(
                        "\nWould you like to refuel during the trip? (Y/N): "
                    ).strip().lower()

                    if choice in ("y", "n"):
                        break

                    print("Invalid option! Please enter Y or N.")

                if max_distance > 0:
                    self.mileage += max_distance
                    remaining_distance -= max_distance
                    self.fuel_level = 0

                    print(f"\nDriven {max_distance:.1f} km.")
                    print(f"Remaining distance: {remaining_distance:.1f} km")

                if choice == "n":
                    print("\nTrip stopped due to insufficient fuel.")
                    print(f"Total mileage: {self.mileage:.1f} km")
                    print(f"Fuel remaining: {self.fuel_level:.1f}%")
                    return

                self.refuel()
                print("\nContinuing the trip...")

            else:
                self.mileage += remaining_distance
                self.fuel_level = max(
                    0, self.fuel_level - remaining_distance * 0.1
                )

                print(f"\nDriven {remaining_distance:.1f} km.")
                remaining_distance = 0

        print("\nTrip completed successfully!")
        print(f"Total mileage: {self.mileage:.1f} km")
        print(f"Fuel remaining: {self.fuel_level:.1f}%")

    # Always refuel the tank to 100%
    def refuel(self):
        if self.fuel_level >= 100:
            print("The tank is already full!")
            return

        fuel_added = 100 - self.fuel_level
        self.fuel_level = 100

        print(f"Refueled {fuel_added:.1f}% of fuel.")
        print("Fuel tank is now full (100%).")

    # Displaying car information
    def show_status(self):
        print(f"\nCar: {self.brand} {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage:.1f} km")
        print(f"Fuel level: {self.fuel_level:.1f}%")


class Fleet:
    def __init__(self):
        self.cars = []

    # Adding a car to the fleet
    def add_car(self, car):
        if car in self.cars:
            print("This car is already in the fleet!")
            return

        self.cars.append(car)
        print(f"{car.brand} {car.model} added to the fleet.")

    # Removing a car from the fleet
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from the fleet.")
        else:
            print("Car not found in the fleet!")

    # Calculating total fleet mileage
    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    # Displaying all cars and fleet statistics
    def show_fleet(self):
        if not self.cars:
            print("\nThe fleet is empty!")
            return

        print("\n===== FLEET STATUS =====")

        for index, car in enumerate(self.cars, start=1):
            print(f"\nCar #{index}")
            car.show_status()

        print("\n========================")
        print(f"Total cars: {len(self.cars)}")
        print(f"Fleet mileage: {self.total_mileage():.1f} km")


# Selecting a car from the fleet
def select_car(fleet):
    if not fleet.cars:
        print("The fleet is empty!")
        return None

    print("\nAvailable cars:")

    for index, car in enumerate(fleet.cars, start=1):
        print(f"{index}. {car.brand} {car.model} ({car.year})")

    try:
        choice = int(input("Select a car number: "))

        if 1 <= choice <= len(fleet.cars):
            return fleet.cars[choice - 1]

        print("Invalid car number!")

    except ValueError:
        print("Please enter a valid number!")

    return None


def main():
    fleet = Fleet()

    # Starting cars
    car1 = Car("Lada", "Niva", 1985)
    car2 = Car("Suzuki", "Swift - Pizzafutár GT", 1995)
    car3 = Car("Opel", "Corsa", 2023)

    # Adding cars to the fleet
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    while True:
        print("\n===== CAR FLEET MANAGER =====")
        print("1. Show fleet")
        print("2. Drive a car")
        print("3. Refuel a car")
        print("4. Add a car")
        print("5. Remove a car")
        print("6. Show total fleet mileage")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ")

        if choice == "1":
            fleet.show_fleet()

        elif choice == "2":
            car = select_car(fleet)

            if car:
                try:
                    distance = float(
                        input("Enter distance in km: ")
                    )
                    car.drive(distance)
                except ValueError:
                    print("Please enter a valid distance!")

        elif choice == "3":
            car = select_car(fleet)

            if car:
                car.refuel()

        elif choice == "4":
            brand = input("Enter car brand: ").strip()
            model = input("Enter car model: ").strip()

            if not brand or not model:
                print("Brand and model cannot be empty!")
                continue

            try:
                year = int(input("Enter production year: "))

                if year < 1886 or year > 2026:
                    print("Invalid production year!")
                    continue

                new_car = Car(brand, model, year)
                fleet.add_car(new_car)

            except ValueError:
                print("Please enter a valid year!")

        elif choice == "5":
            car = select_car(fleet)

            if car:
                fleet.remove_car(car)

        elif choice == "6":
            print(
                f"\nTotal fleet mileage: "
                f"{fleet.total_mileage():.1f} km"
            )

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option! Please choose 1-7.")


if __name__ == "__main__":
    main()
