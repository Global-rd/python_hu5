
class Car:
    #------------------------
    def __init__(self, brand: str, model:str, year:int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0
    #----------------------------
    def drive(self, distance):             # 0,1 % -> 1 km /// 1 % -> 10km)

        if distance <= 0:
            print ("Distance must be positiv or higher than zero!")
            return
        
        if distance > (self.fuel_level * 10):
            print (f"Dont have enough fuel. The limit is {self.fuel_level*10}km")
            return
        
        self.fuel_level -= (distance / 10)
        self.mileage += distance

        print(f"{self.brand} {self.model} "
              f"drove {distance}km."
              f"Total mileage {self.mileage}km, fuel level: {self.fuel_level} % fuel.")
    #----------------------------
    def refuel(self, fuel_refill_level):

        if fuel_refill_level <= 0:
            print(f"Refill amount must be positiv!")
            return
        
        if self.fuel_level + fuel_refill_level > 100:
            print(f"Maximum refill level is {100 - self.fuel_level} °%")
            return
        self.fuel_level += fuel_refill_level

    def display_all_info(self):
        print(f"    Brand:              {self.brand}\n"
              f"    Model:              {self.model}\n"
              f"    Year:               {self.year}\n"
              f"    Mileage:            {self.mileage}\n"
              f"    Left fuel level:    {self.fuel_level}"
              )

#---------------------------------------
    
class Fleet:
    #-------------------------
    def __init__(self):
        self.cars = []
    #--------------------------
    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} {car.year} added to the fleet.")
    #---------------------------
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} {car.year} removed from the fleet.")
        else:
            print(f"{car.brand} {car.model} {car.year} is not in the fleet!")
    #----------------------------
    def total_mileage(self):
        return(sum(i.mileage for i in self.cars))
    #----------------------------
    def display_fleet(self):
        print("********************************\n"
              "***---    Fleet Status    ---***\n"
              "********************************")
        for i in self.cars:
            i.display_all_info()
            print("---")

        print(f"Number of cars: {len(self.cars)}")
        print(f"Total mileage: {self.total_mileage()}")

#--------------------------------------------------

if __name__ == "__main__":
    #-------------------------------------
    # autok letrehozasa
    car1 = Car("Volkswagen", "T1", 1984)
    car2 = Car("Volvo", "V70", 2005)
    car3 = Car("Opel","Zafira", 2010)
    car4 = Car("BMW", "M3", 2000)
    car5 = Car("Trabant", "", 1980)

    # fleet feltoltese
    fleet = Fleet()

    print("\n")

    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    fleet.add_car(car4)
    fleet.add_car(car5)

    print("\n")
    fleet.display_fleet()

    car1.drive(250)
    car2.drive(50)
    car3.drive(100)
    car4.drive(300)
    car5.drive(1000)
    car1.drive(-1)

    print("\n")

    fleet.display_fleet()

    print("\n")

    car1.refuel(10)
    car2.refuel(-1)
    car2.refuel(1000000000)
    car5.refuel(10)

    fleet.display_fleet()

    print("\n")

    fleet.remove_car(car2)

    print("\n")

    fleet.display_fleet()

    print("\n")

    #-----------------------------------------
