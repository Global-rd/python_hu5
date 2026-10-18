"""
Car fleet manager (homework 5).
 
Car:   a single car that can be driven and refueled.
Fleet: manages Car objects. This is composition: a fleet "has" cars,
       it does not inherit from the Car class.
"""
 
MAX_FUEL_LEVEL = 100  # percent
FUEL_PER_KM = 0.1     # percent of fuel used per km driven
 
 
class Car:
    """A car with mileage and fuel level that can be driven and refueled."""
 
    def __init__(self, brand, model, year):
        """
        Set up a new car with an empty odometer and a full tank.
 
        Parameters:
            brand (str): The brand of the car.
            model (str): The model of the car.
            year (int): The year of manufacture.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = MAX_FUEL_LEVEL
 
    def get_name(self):
        """Return the short name of the car, e.g. 'Toyota Corolla'."""
        return f"{self.brand} {self.model}"
 
    def get_range(self):
        """Return how many km the car can still drive with its current fuel."""
        return round(self.fuel_level / FUEL_PER_KM, 2)
 
    def drive(self, distance):
        """
        Drive the given distance, but only as far as the fuel allows.
 
        Parameters:
            distance (int, float): The distance to drive in km.
 
        Returns:
            int, float: The distance actually driven.
 
        Raises:
            ValueError: If the distance is not a positive number.
        """
        if distance <= 0:
            raise ValueError("The distance must be a positive number.")
 
        max_distance = self.get_range()
        if max_distance == 0:
            print(f"{self.get_name()} cannot move: the tank is empty.")
            return 0
 
        if distance > max_distance:
            print(
                f"Not enough fuel for {distance} km. "
                f"{self.get_name()} can only drive {max_distance} km."
            )
            distance = max_distance
 
        self.mileage = round(self.mileage + distance, 2)
        self.fuel_level = max(0, round(self.fuel_level - distance * FUEL_PER_KM, 2))
        print(f"{self.get_name()} drove {distance} km. Fuel left: {self.fuel_level}%")
        return distance
 
    def refuel(self, amount):
        """
        Add fuel to the tank, but never above the maximum level.
 
        Parameters:
            amount (int, float): The amount of fuel to add, in percent.
 
        Returns:
            int, float: The amount of fuel actually added.
 
        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("The refuel amount must be a positive number.")
 
        free_space = round(MAX_FUEL_LEVEL - self.fuel_level, 2)
        if free_space == 0:
            print(f"{self.get_name()}: the tank is already full.")
            return 0
 
        if amount > free_space:
            print(f"{self.get_name()}: only {free_space}% fits in the tank (requested {amount}%).")
            amount = free_space
 
        self.fuel_level = round(self.fuel_level + amount, 2)
        print(f"{self.get_name()} refueled with {amount}%. Fuel level: {self.fuel_level}%")
        return amount
 
    def get_info(self):
        """Return the current state of the car as a string."""
        return (
            f"{self.get_name()} ({self.year}) | "
            f"Mileage: {self.mileage:.1f} km | "
            f"Fuel: {self.fuel_level:.1f}% | "
            f"Range: {self.get_range():.1f} km"
        )
 
 
class Fleet:
    """A fleet that stores and manages Car objects in a list."""
 
    def __init__(self, name="Company fleet"):
        """
        Set up an empty fleet.
 
        Parameters:
            name (str): The name of the fleet.
        """
        self.name = name
        self.cars = []
 
    def add_car(self, car):
        """
        Add a car to the fleet (the same car can't be added twice).
 
        Parameters:
            car (Car): The car to add.
        """
        if car in self.cars:
            print(f"{car.get_name()} is already in the fleet.")
            return
        self.cars.append(car)
        print(f"{car.get_name()} added to the fleet.")
 
    def remove_car(self, car):
        """
        Remove a car from the fleet.
 
        Parameters:
            car (Car): The car to remove.
        """
        if car not in self.cars:
            print(f"{car.get_name()} is not in the fleet.")
            return
        self.cars.remove(car)
        print(f"{car.get_name()} removed from the fleet.")
 
    def get_total_mileage(self):
        """Return the total km driven by all cars in the fleet."""
        return round(sum(car.mileage for car in self.cars), 2)
 
    def get_average_fuel_level(self):
        """Return the average fuel level of the fleet (0 if the fleet is empty)."""
        if not self.cars:
            return 0
        return round(sum(car.fuel_level for car in self.cars) / len(self.cars), 2)
 
    def display_cars(self):
        """Print the current state of every car in the fleet."""
        print(f"\n--- Cars in '{self.name}' ---")
        if not self.cars:
            print("The fleet is empty.")
            return
        for number, car in enumerate(self.cars, start=1):
            print(f"{number}. {car.get_info()}")
 
    def display_summary(self):
        """Print the summary data of the fleet."""
        print(f"\n--- Summary of '{self.name}' ---")
        print(f"Number of cars:     {len(self.cars)}")
        print(f"Total mileage:      {self.get_total_mileage():.1f} km")
        print(f"Average fuel level: {self.get_average_fuel_level():.1f}%")
 
 
def main():
    """Create a few cars, run some operations and display the results."""
    fleet = Fleet("Company fleet")
 
    car_1 = Car("Toyota", "Corolla", 2020)
    car_2 = Car("Skoda", "Octavia", 2018)
    car_3 = Car("Ford", "Focus", 2022)
 
    print("=== Adding cars ===")
    for car in [car_1, car_2, car_3]:
        fleet.add_car(car)
    fleet.add_car(car_1)  # duplicate, will not be added again
 
    print("\n=== Driving ===")
    car_1.drive(150)
    car_2.drive(420)
    car_3.drive(80)
    car_2.drive(700)  # more than the remaining fuel allows
    car_2.drive(10)   # the tank is empty now
 
    print("\n=== Refueling ===")
    car_2.refuel(60)
    car_1.refuel(50)  # only 15% fits
    car_3.refuel(8)
 
    print("\n=== Invalid operations ===")
    try:
        car_3.drive(-10)
    except ValueError as error:
        print(f"Error: {error}")
 
    try:
        car_1.refuel(0)
    except ValueError as error:
        print(f"Error: {error}")
 
    fleet.display_cars()
    fleet.display_summary()
 
    print("\n=== Removing a car ===")
    fleet.remove_car(car_3)
    fleet.remove_car(car_3)  # already removed
 
    fleet.display_cars()
    fleet.display_summary()
 
 
if __name__ == "__main__":
    main()
