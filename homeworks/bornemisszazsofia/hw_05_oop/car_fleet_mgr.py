
class InsufficientFuelLevelError(Exception):
    """
    Custom exception for insufficient fuel level.
    """
    pass

class InvalidInput(Exception):
    """
    Custom exception for invalid mileage/fuel/car input.
    """
    pass


class Car:

    def __init__(self, brand: str, model: str, year: int, mileage = 0, fuel_level = 100):
        self.brand = brand
        self.model = model
        self.year = year
        if mileage >= 0:
            self.mileage = mileage
        else:
            raise InvalidInput("Mileage must be zero or positive.")
        if 0 <= fuel_level <= 100:
            self.fuel_level = fuel_level
        else:
            raise InvalidInput("Fuel level must be between 0 and 100 % when registering the car.")
        

    #def __str__(self):
    #    return f"{self.brand} / {self.model} / {self.year} / {self.mileage} km / {self.fuel_level} %"
    

    def __eq__(self, other_car):
        if isinstance(other_car, Car):
            return self.brand == other_car.brand and self.model == other_car.model and self.year == other_car.year
        return False  
      
   
    def drive(self, mileage):
        if mileage <= 0:
            raise InvalidInput("Driven mileage must be positive.")
        if mileage*0.1 > self.fuel_level:
            raise InsufficientFuelLevelError(f"Not enough fuel. Max. available mileage: {self.fuel_level/0.1}. Please refuel.")
        self.mileage += mileage
        self.fuel_level -= mileage*0.1
        print(f"Mileage of {self.brand} {self.model} ({self.year}) is at {self.mileage} km and fuel tank at {self.fuel_level} %.")

   
    def refuel(self, fuel_amount):
        if fuel_amount <= 0:
            raise InvalidInput("Refill  amount must be positive.")  
        if fuel_amount + self.fuel_level > 100:
            raise InvalidInput(f"Fuel level cannot exceed 100%. You can refuel by a maximum of {100 - self.fuel_level}.")
        self.fuel_level += fuel_amount
        print(f"Fuel tank of {self.brand} {self.model} ({self.year}) is at {self.fuel_level} %.")


class Fleet:


    def __init__(self, name: str):
        self.name = name
        self.fleet = []


    def add_car(self, car: Car):
        if car not in self.fleet:
            self.fleet.append(car)
        else:
            raise ValueError(f"Car with attributes of '{car}' already registered in the fleet.")

    def remove_cars(self, car: Car):
        if car in self.fleet:
            self.fleet.remove(car)
        else:
            raise ValueError(f"No car with attributes of '{car}' found in the fleet.")

    def get_mileage_total(self):
        mileage_total = 0
        for car in self.fleet:
            mileage_total += car.mileage
        return mileage_total

    def list_fleet_cars(self):
        print(f"Cars currently in the {self.name}:")
        for car in self.fleet:
            print(car)



#Car objektumok letrehozasa:
car_1 = Car(brand="Audi", model="A4", year=2023)
car_2 = Car(brand="Ford", model="Puma", year=2021)
car_3 = Car(brand="Tesla", model="Y model", year=2025)
car_4 = Car(brand="Tesla", model="Roadster", year=2026)
car_5 = Car(brand="Hyundai", model="i30", year=2015)
car_6 = Car(brand="Hyundai", model="i20", year=2014)
car_7 = Car(brand="Hyundai", model="i10", year=2024)
car_8 = Car(brand="Hyundai", model="i10", year=2024)

#Flotta 1 letrehozasa es megtekintese:

fleet_1 = Fleet("Private fleet")
fleet_1.add_car(car_1)
fleet_1.add_car(car_2)
fleet_1.list_fleet_cars()

print("----------------------------------------------------------")

#Flotta  letrehozasa es megtekintese:

fleet_2 = Fleet("Company fleet")
fleet_2.add_car(car_3)
fleet_2.add_car(car_4)
fleet_2.add_car(car_5)
fleet_2.list_fleet_cars()

print("----------------------------------------------------------")

#Müveletek a Car objektumokkal:

car_1.drive(465)
car_2.drive(385)
car_3.drive(200)
car_4.drive(100)
car_5.drive(265)

print("----------------------------------------------------------")

car_1.refuel(46)
car_2.refuel(30)
car_3.refuel(10)
car_4.refuel(5)
car_5.refuel(25)

print("----------------------------------------------------------")

print(fleet_1.get_mileage_total())
print(fleet_2.get_mileage_total())

print("----------------------------------------------------------")

car_1.drive(500)
car_2.drive(500)
car_3.drive(500)
car_4.drive(500)
car_5.drive(500)
car_6.drive(600)
car_7.drive(700)

print("----------------------------------------------------------")

#Müveletek Fleet objektummal:

fleet_2.add_car(car_6)
fleet_2.add_car(car_7)

print(fleet_1.get_mileage_total())
print(fleet_2.get_mileage_total())

print("----------------------------------------------------------")

fleet_2.remove_cars(car_5)
fleet_2.remove_cars(car_3)
fleet_2.list_fleet_cars()
print(fleet_2.get_mileage_total())

print("----------------------------------------------------------")

fleet_1.remove_cars(car_1)
fleet_1.list_fleet_cars()
print(fleet_1.get_mileage_total())

print("----------------------------------------------------------")

#Hibakezeles ellenörzese:

#car_6 = Car(brand="Hyundai", model="i20", year=2014, mileage= -400)
#car_7 = Car(brand="Hyundai", model="i10", year=2024, fuel_level= 150)

#car_3.drive(500)

#car_4.refuel(-100)
#car_4.refuel(80)

#fleet_2.remove_cars(car_1)

#print(car_7 == car_8)
#fleet_2.add_car(car_8)

print("----------------------------------------------------------")