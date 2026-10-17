
class Fleet:

    def __init__(self):
        self.cars=[]
    
    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car: Car):
        try:
            self.cars.remove(car)
        except ValueError as ve:
            # Vajon kellene erre is külön custom exceptiont definiálni? 
            print(f'There is no car like this:\n\t{car} \nin the fleet')

    def printlist(self):    
        print('\n'.join(map(str, self.cars)))

    def __str__(self):
       return (
            f'The fleet consists of {len(self.cars)} cars.See the details below\n'
            f'{'\n'.join(map(str, self.cars))}\n'
            f'Fleet mileage: {self.sum_mileage()} kms'
        )
      
    def sum_mileage(self):
        summ=0
        for car in self.cars:
            summ += car.mileage

        return summ
