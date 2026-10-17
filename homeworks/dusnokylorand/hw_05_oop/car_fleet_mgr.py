class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        fuel_needed = distance * 0.1

        if fuel_needed <= self.fuel_level:
            self.mileage += distance
            self.fuel_level -= fuel_needed
        else:
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0

    def refuel(self, amount):
        self.fuel_level += amount

        if self.fuel_level > 100:
            self.fuel_level = 100

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def total_mileage(self):
        total = 0

        for car in self.cars:
            total += car.mileage

        return total
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Focus", 2019)
car3 = Car("BMW", "320i", 2021)

fleet = Fleet()

fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
car1.drive(120)
car2.drive(80)
car3.drive(150)

car1.refuel(20)
car2.refuel(10)
for car in fleet.cars:
    print(
        f"{car.brand} {car.model} ({car.year}) - "
        f"Mileage: {car.mileage} km, "
        f"Fuel level: {car.fuel_level}%"
    )

print(f"Total fleet mileage: {fleet.total_mileage()} km")
