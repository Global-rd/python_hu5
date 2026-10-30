class InsufficientFuelError(Exception):
    """
    Uzemanyag custom exception letrehozasa arra az esetre ha kifogy az uzemanyag
    """
    pass

class TooMuchFuelError(Exception):
    """
    Custom exception arra az esetre ha a refuel tobb lenne mint 100%
    """
    pass

class Car:
    def __init__(self, brand: str, model, year: int, mileage =0, fuel_level=100):
          self.brand = brand
          self.model = model 
          self.year = year
          self.mileage = mileage
          self.fuel_level = fuel_level
    def drive(self, km):
         #eloszor ellenorizni, mert ha utana, akkor mar levonta az uzemanyagot
         if km*0.1 > self.fuel_level:  
            raise InsufficientFuelError ("Not enough fuel!")
         self.mileage += km
         self.fuel_level -=km*0.1
    def refuel (self, refuel_amount):
        # tank + amit hozzaadok, nem lehet tobb, mint 100 
        if self.fuel_level + refuel_amount > 100:
            raise TooMuchFuelError ("Too much fuel!")
        self.fuel_level += refuel_amount
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage} - {self.fuel_level}%"

class Fleet:
    def __init__(self):
        # a flottanak VANNAK autoi, a listaban egesz Car objektumok vannak 
        self.cars = []
    def add_car(self, car: Car):
        self.cars.append(car)
        #itt nem kell loop, a remove a memoria cim alkapjan talalja meg ugyanazt az objektumot 
    def remove_car(self, car:Car):
        self.cars.remove(car)
    def total_mileage(self):
        total = 0 #normal variable, nem self.total, mert csak addig kell amig a method fut 
        for car in self.cars: 
            total += car.mileage
        return total
         

car_1 = Car("Audi", "A5", 2000)
#try/except, hogy a program ne alljon le, ha nincs eleg uzemanyag 
try:
    car_1.drive(500)
except InsufficientFuelError as e:
    print(e)
try:    
    car_1.refuel(30)
except TooMuchFuelError as e:
    print(e)

car_2 = Car("Toyota", "Corolla", 2006)
car_2.drive(200)


print(car_1)
print(car_2)

fleet_1 = Fleet()
fleet_1.add_car(car_1)
fleet_1.add_car(car_2)
for car in fleet_1.cars:
    print(car)
print(fleet_1.total_mileage())

fleet_1.remove_car(car_1) 

for car in fleet_1.cars:
    print(car)
