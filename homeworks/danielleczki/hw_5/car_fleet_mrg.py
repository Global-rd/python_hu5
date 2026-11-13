class Car:
    def __init__(self, brand:str, model:str, year:str, milage:int=0, fuel_level:int=100) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.milage = milage
        self.fuel_level = fuel_level

    def drive(self, distance:int):
        if self.fuel_level < distance or distance <= 0:
            print("Nem elég az üzemanyag, vagy helytelen számot adtál meg!")
            return
        self.fuel_level -= distance
        self.milage += distance

    def refuel(self, amount:int):
        if amount <= 0 or self.fuel_level + amount > 100:
            print("Nem lehet ennyit tankolni!")
            return
        self.fuel_level += amount

class Fleet():
    def __init__(self, name:str):
        self.name = name
        self.cars = []
    def remove_car(self,car:Car):
        if car in self.cars:
            self.cars.remove(car)
            return
                
    def add_car(self,car:Car):
        self.cars.append(car)
        
    def all_fleet_km(self):
        all_km = 0
        for car in self.cars:
            all_km += car.milage
        return all_km
    
car_1 = Car("toyota", "Corolla", "1996", 0, 20)
car_2 = Car("bmw", "e60", "1986", 0, 20)
car_fleet_1 = Fleet("Jó kocsik")
car_1.drive(10)
car_1.refuel(0)
print("-------------------------------------------")
print(f"Az autó megtett távólsága: {car_1.milage}")
print(f"Az autó jelenlegi üzemanyagszintje: {car_1.fuel_level}%")
print("-------------------------------------------")

car_fleet_1.add_car(car_1)
car_fleet_1.add_car(car_2)

print("Eltávolítás előtt:")
for car in car_fleet_1.cars:
    print(car.brand, car.model)

car_fleet_1.remove_car(car_1)

print("Eltávolítás után:")
for car in car_fleet_1.cars:
    print(car.brand, car.model)

print(Fleet.all_fleet_km(car_fleet_1))