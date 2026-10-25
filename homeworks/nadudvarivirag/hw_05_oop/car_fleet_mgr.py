#mileage - megetett km-t tárolja
#rendszám, ami alapján törlünk
class Car:
    def __init__(self, brand:str, modell:str, year:int, licence_plate:str, mileage:int=0, fuel_level:float=100):
        self.brand = brand
        self.modell = modell
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
        self.licence_plate = licence_plate

    def __str__(self):
        return f"{self.brand}, {self.modell}, {self.year}, {self.mileage}, {self.fuel_level}, {self.licence_plate}"

    def drive(self, km:int):
        if km  < 0:
            print("Invalid distance. It must be a positive number!")
            return 
        #először kiszámoljuk hogy az aktuális benzin mennyiséggel mennyit tudunk menni?
        max_distance = self.fuel_level / 0.1
        if km > max_distance:
            print("Not enough fuel")
            return
        else:
            self.mileage += km
            self.fuel_level -= km * 0.1
        
        

    def refuel(self, fuel_quantity): #limitre figyelni
        if fuel_quantity < 0:
            print("Invalid fuel quantity")
            return
        if self.fuel_level + fuel_quantity > 100:
            print("Overload fuel")
            return
        else:
            self.fuel_level += fuel_quantity

class Fleet:
    def __init__(self):
        self.cars = []
    

    def add_car(self, car: Car):
        self.cars.append(car)

    #Egyedi azonosító (rendszám) alapján törlünk 
    def remove_car(self, licence_plate: str):
        for car in self.cars:
            if car.licence_plate == licence_plate:
                self.cars.remove(car)
                print(f"The car was successfully removed based on the license plate: {licence_plate}.")
                return
        print(f"Car not found with this licence plate: {licence_plate}")
    
    def sum_mileage_car(self):
         total = sum(car.mileage for car in self.cars)
         print (f"The total mileage is: {total} km")
         return total

    #Ennek itt utána néztem, hogyan lehet formázni kicsit
    def list_car(self):
        print(f"The list of the cars in the fleet: ")
        print("-" * 90)
        print(f"{'No.':<5} {'Brand':<12} {'Model':<12} {'Year':<8} {'Mileage (km)':<15} {'Fuel (%)':<12} {'Licence plate'}")
        print("-" * 90)
        for i, car in enumerate(self.cars, start=1):
            print(f"{i:<5} {car.brand:<12} {car.modell:<12} {car.year:<8} {car.mileage:<15} {car.fuel_level:<12} {car.licence_plate}")   
        print("-" * 90)

