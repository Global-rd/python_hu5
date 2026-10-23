class Car:
    def __init__(self, brand:str, model:str, year:int, mileage:float, fuel_level:float):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, km:float=0.0, fuel_level=100.0):

        """Egy drive metodus amely adott szamu kilometerrel noveli
        a km ora allasat es csokkenti az uzemanyagszintet.
        Tetelezzuk fel hogy 0.1% uzemanyag fogy megtette km-kent.
        Csak annyi km-t enged vezetni emnnyire eleg uzemanyag van.
        km ora kiindulo allasa: 0
        Uzemanyag szint indulo erteke: 100"""
        
        if km < 0:
            raise ValueError ("The driven distance can't be less than 0. Please enter a number that is equal or higher than 0!")
        if self.fuel_level < km*0.1:
            raise ValueError (f"{self.brand} {self.model} {self.year} doesn't have sufficient fuel level for the mileage you have entered.")

        self.mileage += km
        self.fuel_level -= km*0.1

    def refuel (self, refuel_percentage:float):

        """Refuel metodus,
        amely feltolti az uzemanyag-szintet egy adott mennyiseggel"""

        if refuel_percentage < 0:
            raise ValueError ("Refuelled amount can't be less than 0. Please enter a valid number!")
        
        if refuel_percentage > 100-self.fuel_level:
            raise ValueError (f"{self.brand} {self.model} doesn't have sufficient tank space for requested fuel amount of {refuel_percentage}")

        self.fuel_level += refuel_percentage

class Fleet:
    def __init__(self):
        self.fleet = []

    """Az osztaly rendelkezzen agy listaval amelyben az autok talalhatok"""

    def add_car(self, car:Car):
        
        self.fleet.append(car)


    """Metodus Car objektumok hozzaadasara"""

    def remove_car(self, removed_car):
        for car in self.fleet:
            if removed_car == car:
                self.fleet.remove(car)
                return
        print(f"Car {removed_car} could not be removed, as it is not found in the fleet!")

        """Metodus Car objektum eltavolitasara"""

    def total_mileage(self):
        return sum(car.mileage for car in self.fleet)

    """Metodus, amely osszesiti a flotta osszes autojanak osszes km-et"""
   
    def list_cars(self):
        
        if not self.fleet:
            print("The fleet is empty.")
            return

        print("Current cars in the fleet:")
        for car in self.fleet:
            print(
                f"{car.brand} {car.model} ({car.year}) — "
                f"{car.mileage:g} km, {car.fuel_level:g}% fuel"
            )

    """Autok listaja"""

#Objektumok letrehozasa:
car_1 = Car("Tesla", "Model Y", 2024, 0, 100)
car_2 = Car("Nissan", "Leaf", 2021, 0, 100)
car_3 = Car("Ford", "Focus", 2018, 0, 100)
car_4 = Car("Toyota", "Yaris", 2020, 0, 100)

#Autok hozzaadasa a flottahoz:
fleet = Fleet()
fleet.add_car(car_1)
fleet.add_car(car_2)
fleet.add_car(car_3)
fleet.add_car(car_4)

#Autok vezetese:
car_1.drive(345)
car_2.drive(265)
car_3.drive(532)
car_4.drive(122)

#Autok tankolasa:
car_1.refuel(23)
car_2.refuel(25)
#hibauzenet mukodik: ValueError: Nissan Leaf doesn't have sufficient tank space for requested fuel amount of 33. Kijavitva 25-re.
car_3.refuel(44)
car_4.refuel(4)

#Auto eltavolitasa
fleet.remove_car(car_3)

fleet.list_cars()
fleet.total_mileage()


            
            