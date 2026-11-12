class NoFuelError(Exception):
    """
    Custom exception for no fuel 
    """
    pass

class DistanceError(Exception):
    """
    Custom exception for too big distance
    """
    pass

class MaxFuelError(Exception):
    """
    Custom exception for maximum fuel
    """
    pass

class FuelOverloadError(Exception):
    """
    Custom exception for too much fuel
    """
    pass

# Here's the car class with all the methods
class Car:
    # Let's create a car
    def __init__(self, brand: str, model: str, year: int, mileage: int=0, fuel_level: float=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    # Let's make the car object readable for a human being
    def __str__(self):
            return f"{self.brand} - {self.model} -  {self.year}"

    # Drive around and catching some errors
    def drive(self, distance: int):
        if distance <= 0:
            raise ValueError("Distance must be positive!")
        if self.fuel_level <= 0:
            raise NoFuelError("Not enough fuel to drive!")
        if distance > self.fuel_level * 10:  
            raise DistanceError("Not enough fuel to drive the requested distance!")
        self.mileage += distance
        self.fuel_level -= distance / 10
        return f"{self.brand} {self.model} has driven {self.mileage:} km"

    # Refualing after the fun
    def refuel(self, amount: float):
        if amount <= 0:
            raise ValueError("Refuel amount must be positive!")
        if self.fuel_level >= 100:
            raise MaxFuelError("Fuel level is already full!")
        if self.fuel_level + amount > 100:
            raise FuelOverloadError("Fuel level cannot exceed 100%!")
        self.fuel_level += amount

    # Why not fill it to the max, right?
    def max_refuel(self):
        if self.fuel_level >= 100:
            raise MaxFuelError("Fuel level is already full!")
        print(f"Maximum refuel amount: {100 - self.fuel_level}%")
        self.fuel_level = 100

# Another object based on the composotion lesson
class Fleet:

    def __init__(self, name: str):
        self.name = name
        self.cars = []

    # adding cars to the fleet
    def add_car(self, car: Car):
        self.cars.append(car)

    # Listing the cards
    def list_cars(self):
        print(f"Available cars in {self.name}")
        for car in self.cars:
            print(car)

    # Removing a car
    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            return
        print(f"No car found in {self.name}")

    # Sum the mileage in the fleet
    def sum_mileage(self):
        temp_sum_mileage = 0
        for car in self.cars:
            temp_sum_mileage += car.mileage
        return temp_sum_mileage


def Main():
    # Let's create a fleet
    fleet = Fleet("My Car Fleet")
    # Let's create some cars 
    car1 = Car("Toyota", "Camry", 2020, 20, 0)
    car2 = Car("Honda", "Civic", 2019, 70, 100)
    car3 = Car("Ford", "Mustang", 2021, 0, 100)
    car4 = Car("Chevrolet", "Malibu", 2018, 10, 100)
    car5 = Car("Nissan", "Altima", 2022, 20, 100)

    # Let's add those cars to the fleet
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    fleet.add_car(car4)
    fleet.add_car(car5)

    # List all the cars
    fleet.list_cars()

    # Use the total milage method
    print(f"Total mileage of our fleet: {fleet.sum_mileage()} km")

    # Let's drive around and testing my exceptions
    try:
        car1.drive(0)
    except ValueError as error:
        print(f"Proper number, please: {error}")
    except NoFuelError as error:
        print(f"Empty tank: {error}")
    except DistanceError as error:
        print(f"Can't go that far: {error}")

    try:
        car1.drive(100)
    except ValueError as error:
        print(f"Proper number, please: {error}")
    except NoFuelError as error:
        print(f"Empty tank: {error}")
    except DistanceError as error:
        print(f"Can't go that far: {error}")
        
    try:
        car2.drive(1000000)
    except ValueError as error:
        print(f"Proper number, please: {error}")
    except NoFuelError as error:
        print(f"Empty tank: {error}")
    except DistanceError as error:
        print(f"Can't go that far: {error}")

    try:
        car3.drive(100)
    except ValueError as error:
        print(f"Proper number, please: {error}")
    except NoFuelError as error:
        print(f"Empty tank: {error}")
    except DistanceError as error:
        print(f"Can't go that far: {error}")    

    # Do the same with the refuel
    try:
        car5.max_refuel()
    except MaxFuelError as error:
        print(f"Already full: {error}") 

    try:
        car3.max_refuel()
    except MaxFuelError as error:
        print(f"Already full: {error}") 

    try:
        car1.refuel(50)
    except ValueError as error:
        print(f"Just pump something in: {error}") 
    except MaxFuelError as error:
        print(f"Already full: {error}") 
    except FuelOverloadError as error:
        print(f"It's not an SUV: {error}") 

Main()