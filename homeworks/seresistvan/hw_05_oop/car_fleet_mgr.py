class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, km):
        if km <= 0:
            print("The range needs to be a positive value.")
            return

        max_km = self.fuel_level / 0.1
        if km > max_km:
            km = max_km
            print("There are not enough fuel left.")

        self.mileage += km
        self.fuel_level -= km * 0.1
        if self.fuel_level < 0:
            self.fuel_level = 0




class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):


    def total_mileage(self):


    def show_cars(self):



