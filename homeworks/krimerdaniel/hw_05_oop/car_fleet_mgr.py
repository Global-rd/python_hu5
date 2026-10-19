"""
A car fleet manager script

Allows create Car type object and fleet type objects, where fleet type object works with Car attributes.

"""

import os
os.system("cls")
from logging_setup import setup_logging
import logging


setup_logging()
logger = logging.getLogger(__name__)


class Car:

    def __init__ (self, brand: str, model: str, year: int, mileage: float = 0.0, fuel_level: float = 100.0):
        self.brand = brand
        self.model = model
        self.year = year            
        self.mileage = mileage
        self.fuel_level = fuel_level
        self._fuel_consumption = 0.1
        self._min_fuel_level = 0.0
        self._max_fuel_level = 100.0
        logger.info(f"Car {self.brand} is successfully created.")

    def drive(self, distance: float):
        if distance <= 0:
            logger.error(f"{distance} is invalid distance, drive function cannot be applied.")
        elif self.fuel_level / self.fuel_consumption < distance:
            logger.warning(f"The {self.brand} cannot drive {distance} miles, because it has enough fuel for {self.fuel_level / self.fuel_consumption} miles only.")
        else:
            self.mileage += round(distance, 2)
            self.fuel_level -= round((distance * self.fuel_consumption), 2)
            logger.info(f"On {self.brand} drive function applied {distance}.")
        

    def refuel(self, refuel_qty: float):
        if refuel_qty <= 0:
            logger.error(f"{refuel_qty} is invalid refuel quantity, refuel function cannot be applied on.")
        elif refuel_qty > self.max_fuel_level - self.fuel_level:
            logger.warning(f"There is not enough space in the fuel tank, the maximum quantity to refuel is {self.max_fuel_level - self.fuel_level}, but not {refuel_qty}.")
        else:
            self.fuel_level += round(refuel_qty, 2)
            logger.info(f"On {self.brand} refuel function applied {refuel_qty}.")


class Fleet():

    def __init__(self, name: str):
        self.name = name
        self.cars = []
        self.total_miles = 0
        logger.info(f"Fleet {self.name} is successfully created.")

    def add_car(self, car: Car):
        """
        This function expects the Car object itself as input instead of sets of its attributes. It takes less typing, and reduces error possibilities.
        """
        if car not in self.cars:
            self.cars.append(car)
            logger.info(f"On {self.name} add_car function applied {car.brand}-{car.model}.")
        else:
            logger.warning(f"Car {car.brand}-{car.model} is already in {self.name}, add_car method cannot be applied.")

    def remove_car(self, car: Car):
        """
        This function expects the Car object itself as input instead of sets of its attributes. It takes less typing, and reduces error possibilities.
        """
        if car in self.cars:
            self.cars.remove(car)
            logger.info(f"On {self.name} remove_car funution applied {car.brand}-{car.model}.")
        else:
            logger.warning(f"This car ({car.brand}-{car.model}) is not in {self.name}, remove_car method cannot be applied.")

    def display_fleet(self):
        """
        This function returns a list where each item is a tuple of (brand, model, year) a Car object.
        """
        if self.cars ==[]:
            logger.warning(f"{self.name} has no cars.")
        else:
            fleet_cars = []
            for car in self.cars:
                fleet_cars.append((car.brand, car.model, car.year))
            print(f"{self.name} cars: {fleet_cars}.")
            logger.info(f"On {self.name} display_fleet funution applied.")

    def total_mileage(self):
        if self.cars == []:
            logger.warning(f"{self.name} has no cars, total_mileage function cannot be applied.")
        else:
            self.total_miles = 0
            for car in self.cars:
                self.total_miles += round(car.mileage, 2)
            print(f"{self.name} total mileage is: {self.total_miles}.")
            logger.info(f"On {self.name} total_mileage funution applied.")
            return self.total_miles      
        


car_1 = Car("Volvo", "XC60", 2025)
car_2 = Car("Fiat", "Punto", 2014)
car_3 = Car("Honda", "CR-V", 2018)
car_4 = Car("Toyota", "Land Cruiser", 2021)
car_5 = Car("Audi", "A6", 2020)

fleet_1 = Fleet("fleet_1")
fleet_2 = Fleet("fleet_2")
fleet_3 = Fleet("fleet_3")


car_1.drive(793.6)
print(round(car_1.mileage, 2))
print(round(car_1.fuel_level, 2))
car_1.refuel(49.69)
print(car_1.fuel_level)

car_2.drive(348.6)
print(round(car_2.mileage, 2))
print(round(car_2.fuel_level, 2))
car_2.drive(461.8)
car_2.drive(455)
print(round(car_2.mileage, 2))
print(round(car_2.fuel_level, 2))
car_2.refuel(76.3)
print(round(car_2.fuel_level, 2))

car_4.drive(211.1)
print(round(car_4.mileage, 2))
print(round(car_4.fuel_level, 2))
car_4.drive(434.0)
print(round(car_4.mileage, 2))
print(round(car_4.fuel_level, 2))
car_4.refuel(9.9)
car_4.refuel(-69.4)
car_4.refuel(69.4)
print(round(car_4.fuel_level, 2))

print("_____________________")

fleet_1.add_car(car_1)
fleet_1.add_car(car_5)
fleet_1.add_car(car_4)
fleet_2.add_car(car_2)
fleet_2.add_car(car_3)
fleet_1.add_car(car_5)
fleet_1.display_fleet()
fleet_2.display_fleet()

fleet_1.total_mileage()
fleet_2.total_mileage()
fleet_1.remove_car(car_1)
fleet_2.remove_car(car_1)
fleet_1.total_mileage()
fleet_3.total_mileage()    