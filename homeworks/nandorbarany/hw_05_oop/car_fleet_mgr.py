
class Car:
    def __init__(self, brand, model, year, mileage=0, fuel_level=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} (Mileage: {self.mileage}, Fuel level: {self.fuel_level:.2f}%)"

    def drive(self, distance):
        if distance <= 0:
            print("Distance must be a positive number.")
            return
        if self.fuel_level <= 0:
            print(f"{self} cannot drive. Fuel level is too low.")
            return

        fuel_consumption = distance * 0.1  # 0.1% fuel consumption per kilometer

        if fuel_consumption > self.fuel_level:
            print(f"{self} cannot drive {distance} kilometer(s). Not enough fuel.")
            return

        self.mileage += distance
        self.fuel_level -= fuel_consumption
        print(f"{self} has driven {distance} kilometer(s). New mileage: {self.mileage}, Fuel level: {self.fuel_level:.2f}%")

    def refuel(self, amount):
        if amount <= 0:
            print(f"Refuel of {self} is only possible with a positive amount.")
            return

        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100
        print(f"{self} refueled. New fuel level: {self.fuel_level:.2f}%")

class Fleet:

    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        if isinstance(car, Car):
            self.cars.append(car)
            print(f"{car} added to the fleet.")
        else:
            print("Only car objects can be added to the fleet.")

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"\n{car} is removed from the fleet.")
        else:
            print(f"{car} is not in the fleet.")

    def list_cars(self):
        result = ""
        print("\nCars in the fleet:")
        for car in self.cars:
            result += f"- {car}, Mileage: {car.mileage}, Fuel level: {car.fuel_level:.2f}%\n"
        print(result)
        if not self.cars:
            print("The fleet is empty.")
        return result

    def kilometers_by_fleet(self):
        total_kilometers = sum(car.mileage for car in self.cars)
        print(f"\nTotal driven kilometers by the fleet: {total_kilometers}")
        return total_kilometers

kia = Car("Kia", "Ceed", 2024, 10000, 80)
porsche = Car("Porsche", "911", 2023, 5000, 90)
ford = Car("Ford", "Mustang Mach 1", 2022, 20000, 60)
dodge = Car("Dodge", "Viper", 2021, 15000, 85)

fleet = Fleet()
fleet.add_car(kia)
fleet.add_car(porsche)
fleet.add_car(ford)
fleet.add_car(dodge)

kia.drive(100)
kia.refuel(20)
porsche.drive(50)
porsche.refuel(10)
ford.drive(200)
ford.refuel(15)
dodge.drive(75)
dodge.refuel(25)
dodge.drive(100)

print(kia)
print(porsche)
print(ford)
print(dodge)

fleet.list_cars()
fleet.kilometers_by_fleet()

fleet.remove_car(ford)
fleet.list_cars()
fleet.kilometers_by_fleet()




