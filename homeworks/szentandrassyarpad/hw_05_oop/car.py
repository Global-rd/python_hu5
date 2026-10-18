
class FuelOverloadException(Exception):
    """
    Custom exception 
    """
    pass

class NotEnoughFuelException(Exception):
    """
    Custom exception
    """
    pass


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.00
        

    def drive(self, kms ):
        if kms*0.1 > self.fuel_level:
            raise NotEnoughFuelException(f'There is not enough fuel in the tank to drive {kms} kms ')
        else:
            self.fuel_level -= kms*0.1
            self.mileage += kms
            

    def refuel(self, pctage: float):
        if self.fuel_level+pctage <= 100.00:
            self.fuel_level += pctage
        else:           
            raise FuelOverloadException('Fuel tank is overloaded, fire hazard!')

    def __str__(self):
         return f'{self.brand}  {self.model} ({self.year}) - {self.mileage} km - {self.fuel_level}% tank'
