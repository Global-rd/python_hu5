class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100



    def drive(self, km):
        if km <= 0:
            print("The distance needs to be positive.")
            return

        max_km = self.fuel_level / 0.1
        if km > max_km:
            km = max_km
            print("Not enough fuel.")

        self.mileage += km
        self.fuel_level -= km * 0.1
        if self.fuel_level < 0:
            self.fuel_level = 0


    def refuel(self, amount):
        if amount <= 0:
            print("The fueled value needs to be positive.")
            return

        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100


    def show_info(self):
        print(self.brand, self.model, "(", self.year, ")")
        print("Mileage:", round(self.mileage, 1), "km")
        print("Fuel:", round(self.fuel_level, 1), "%")
        print()


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
        else:
            print("This car doesn't exist.")

    def total_mileage(self):
        total = 0
        for car in self.cars:
            total += car.mileage
        return total

    def show_cars(self):
        for car in self.cars:
            car.show_info()


fleet = Fleet()

car1 = Car("Tesla", "Model 3", 2025)
car2 = Car("Toyota", "Corolla", 2020)
car3 = Car("Volkswagen", "Golf", 2018)

fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(120)
car2.drive(300)
car2.refuel(20)
car3.drive(1100)

print("Cars of the fleet are:")
fleet.show_cars()
print("All kilometers done by the fleet:", round(fleet.total_mileage(), 1), "km")

fleet.remove_car(car3)
print("Remaining km after a card has been removed:", round(fleet.total_mileage(), 1), "km")