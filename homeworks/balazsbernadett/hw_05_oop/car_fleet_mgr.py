class Car:

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance: int) ->None:
        if distance < 0:
            raise ValueError("Distance can't be negative")
        max_distance = self.fuel_level / 0.1
        print(f"You can drive: {max_distance} km")
        if distance > max_distance:
            print("You can't go that far.")
        else:
            self.mileage += distance
            self.fuel_level -= distance * 0.1

    def refuel(self, add_fuel: int) -> None:
        if add_fuel <0:
            raise ValueError("Can't be negative")
        if self.fuel_level + add_fuel > 100:
            print(f"You can't add that much")
        elif self.fuel_level + add_fuel <= 100:
            self.fuel_level += add_fuel
            print(f"After refueling, the amount is {self.fuel_level}")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, Fuel: {self.fuel_level}%"

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car) ->None:
        self.cars.append(car)
        print(f"add this car: {car.brand} {car.model}")

    def remove_car(self, brand, model) ->None:
        for car in self.cars:
            if car.brand == brand and car.model == model:
                self.cars.remove(car)
                print(f"delete this car: {brand} {model}")
                return
        print(f"There is no this car.: {brand} {model}")

    def total_mileage(self)-> int:
        total = 0
        for car in self.cars:
            total += car.mileage
        print(f"total mileage: {total}")
        return total
car1 = Car("WV", "polo", 2000)
print(car1)
car1.drive(500)
print(f"after drive your fluel: {car1.fuel_level}")
car1.refuel(40)
print(f"after refuel your fluel: {car1.fuel_level}")
car2 = Car("Opel", "I7", 1997)
print(car2)
car2.drive(700)
print(f"after drive your fluel: {car2.fuel_level}")
car2.refuel(30)
print(f"after refuel your fluel: {car2.fuel_level}")
car3 = Car("Mini", "Cooper", 2003)
fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

fleet.remove_car("Mini", "Cooper")
fleet.total_mileage()

print("Flotta's cars:")
for auto in fleet.cars:
    print(auto)