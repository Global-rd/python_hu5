from datetime import datetime as dt
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

#Egy car osztály készítése, amely az autóra jellemző tulajdonságokkal rendelkezik
class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: int=0, _fuel_level: float=100):
        
        if type(year) is not int:
            raise TypeError("Year must be an integer.")

        if type(mileage) is not int:
            raise TypeError("Mileage must be an integer.")

        if mileage < 0:
            raise ValueError("Mileage cannot be negative.")
        
        if not 1900 <= year <= dt.now().year:
            raise ValueError("Invalid manufacturing year.")

        if not 0 <= _fuel_level <= 100:
            raise ValueError("Fuel level must be between 0 and 100.")
        
        self.brand = brand
        self.model = model
        self.year = year 
        self.mileage = mileage
        self.fuel_level = _fuel_level

    def drive(self, km: int):
        """
        Increasing the mileage with a given km, while decreasing the fuel_level
        """

        if type(km) is not int:
            raise TypeError("Km must be an integer.")
        
        #Kiszámolom mennyi km-t lehet megtenni még az üzemanyagszint alapján
        max_mileage = self.fuel_level / 0.1

        #Csak annyi km-t engedjen megtenni, amennyire elegendő üzemanyag van

        if km <= 0:
            raise ValueError("The given km must be greater than 0")
        
        elif km > max_mileage:
            km = max_mileage
            raise ValueError(f"You can drive only {km} km.")
        
        # Növeljük a kilométeróra állását
        self.mileage += km

        #Üzemanyagszint ellenőrzés, szint csökkentés
        if 0 < self.fuel_level - km * 0.1:
            self.fuel_level = self.fuel_level - km * 0.1
        else: 
            self.fuel_level = 0

    def refuel(self, refuel_amount: int):
        """
        Increase the fuel level by a given amount.
        """
        if type(refuel_amount) is not int:
            raise TypeError("Refuel amount must be an integer.")

        #Üzemanyag ellenőrzése és feltöltése

        if refuel_amount <= 0:
            raise ValueError("The refuel amount must be greater than 0")
            return
        elif 100 < self.fuel_level + refuel_amount:
            self.fuel_level = 100
            print(f"The refuel amount: {refuel_amount} exceeds the tank capacity")
        else:
            self.fuel_level += refuel_amount

class Fleet:
    def __init__(self):
        self.cars = []

    #Autó hozzáadása a flottához
    def add_cars(self, car: Car):
        self.cars.append(car)

    #Autó törlése a flottából
    def remove_cars(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print("Removed is succesfully")
        else:
            print("Car not found in the fleet.")

    #összesíti a flotta összes autójának összes kilométerét
    def fleet_total_miles(self, total_miles: int = 0):
        self.total_miles = total_miles

        for car in self.cars:
            total_miles += car.mileage
        return total_miles

    def display_cars(self):
        for car in self.cars:
            print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Mileage: {car.mileage} km, Fuel: {car.fuel_level}%")

#Autók létrehozása
car_1 = Car("VW", "Golf", 2000, 250)
car_2 = Car("Skoda", "Octavia", 2024, 350, 80)
car_3 = Car("Opel", "Astra", 2026, 250, 60)

#Autók vezetése
car_1.drive(300)
car_2.drive(400)
car_3.drive(50)

#Autókba tankolás
car_1.refuel(20)
car_2.refuel(10)
car_3.refuel(8)

cars = Fleet()

#Autók flottához adása
cars.add_cars(car_1)
cars.add_cars(car_2)
cars.add_cars(car_3)

#Autók megjelenítése
cars.display_cars()

#Total flotta kilométer
print(f"Total fleet mileage: {cars.fleet_total_miles()} km")