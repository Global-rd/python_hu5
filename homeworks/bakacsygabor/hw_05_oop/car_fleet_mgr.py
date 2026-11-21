class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        if distance <= 0:
            print("Distance must be a positive number.")
            return

        if self.fuel_level <= 0:
            print("There is no fuel left. Please refuel before driving.")
            return

        max_distance = self.fuel_level / 0.1
        actual_distance = min(distance, max_distance)

        self.mileage += actual_distance
        self.fuel_level = max(0, self.fuel_level - actual_distance * 0.1)

        if actual_distance < distance:
            print("There was only enough fuel for a shorter trip.")

        print(f"The car drove {actual_distance} km.")

    def refuel(self, amount):
        if amount <= 0:
            print("Fuel amount must be positive.")
            return

        if self.fuel_level == 100:
            print("The tank is already full.")
            return

        self.fuel_level = min(100, self.fuel_level + amount)
        print(f"Fuel level: {self.fuel_level}%.")


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added {car.brand} {car.model} to the fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car.brand} {car.model} from the fleet.")
        else:
            print("This car is not in the fleet.")

    def total_mileage(self):
        total = 0

        for car in self.cars:
            total += car.mileage

        return total


def main():
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Ford", "Focus", 2018)
    car3 = Car("Honda", "Civic", 2022)

    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    car1.drive(120)
    car2.drive(250)
    car2.refuel(15)
    car3.drive(80)

    print("\nCars in the fleet:")
    for car in fleet.cars:
        print(
            f"{car.brand} {car.model} ({car.year}) - "
            f"Mileage: {car.mileage} km, fuel: {car.fuel_level}%"
        )

    print(f"Total fleet mileage: {fleet.total_mileage()} km")

    fleet.remove_car(car3)
    print(f"Total mileage after removal: {fleet.total_mileage()} km")


if __name__ == "__main__":
    main()
