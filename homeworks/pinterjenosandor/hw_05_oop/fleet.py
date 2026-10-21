class Car:
    def __init__(self, brand, model, year):  # constructor of car
        self.brand = brand #the brand of the car manufacturer
        self.model = model #the model of the car brand
        self.year = year #the year when the car made
        self.mileage = 0 #the odometer reading default value 0
        self.fuel_level = 100.0  #the level of fuel tank, default state is 100 litre because the consumption is 0.1 litre/km

    def drive(self, distance):
        km_litre = 0.1 #the car consumption / kilometer
        required_fuel = distance * km_litre #driving distance calulation by consumption

        if self.fuel_level <= 0: # check the tank, if it's empty we cannot drive it
            print(f"You cannot drive the car, because the {self.brand} {self.model}'s tank is empty!")
            return 0

        actual_km = distance if required_fuel <= self.fuel_level else self.fuel_level / km_litre
        self.fuel_level -= actual_km * km_litre

        if actual_km < distance:
            print(f"After running {actual_km:.1f} km, the tank became empty!")

        self.mileage += actual_km
        print(
            f"-> {self.brand} {self.model} drove {actual_km:.1f} km. Odometer: {self.mileage:.1f} km, Fuel: {self.fuel_level:.1f}%")
        return actual_km

    def refueling(self, gasoline):
        if gasoline < 0:
            print("Please add a positive number, because the refueling amount cannot be negative")
            return

        old_fuel = self.fuel_level
        self.fuel_level += gasoline

        if self.fuel_level > 100.0:
            self.fuel_level = 100.0
        """
        In this point count the inload fuel, example if tank has 75 litres of gasoline and we try to fill up with 50 litres,
        this section is count and load 25 litres and feedback the required fill up is too much
        """
        added_fuel = self.fuel_level - old_fuel

        if added_fuel < gasoline:
            print(
                f"You requested {gasoline:.1f} litre(s), but we could only add {added_fuel:.1f} liters because the tank is full! Current level: {self.fuel_level:.1f}litre(s)")
        else:
            print(f"The tank is already filled up! Added {added_fuel:.1f} litre(s). Current tank level: {self.fuel_level:.1f}litre(s) ;  {self.fuel_level:.1f}%")

    def __str__(self): #car info
        return f"Vehicle: {self.year} {self.brand} {self.model}, Running distance total: {self.mileage:.1f} km(s), Current fuel level: {self.fuel_level:.1f}litre(s)"


class Fleet:
    def __init__(self): #the fleet basically a list
        self.vehicles = [] #list of the cars

    def add_vehicle(self, car): #add car to the list
        self.vehicles.append(car) #add car to the list via append
        print(f"New car added to the fleet: {car.brand} {car.model}") # text the car added to the list

    def rem_vehicles(self, index):
        if 0 <= index < len(self.vehicles): # check the ID of the car is available or not
            removed = self.vehicles.pop(index) #remove the car from the list via pop
            print(f"The {removed.brand} {removed.model} has been removed from the list.")
        else:
            print("Invalid Car ID! Please check!") #feedback text if the ID of the car is not available

    def total_mileage(self):
        return sum(car.mileage for car in self.vehicles) #sum of the car mileage

    def current_status(self):
        print("\nCurrent status of the fleet:") #Title with enter press
        if not self.vehicles:
            print("The fleet list is currently empty, please add a car!")
        else:
            for idx, car in enumerate(self.vehicles, start=1):
                print(f"{idx}. {car}")
            print(f"The total running of the Fleet: {self.total_mileage():.1f} km\n")


def choose_menu():
    choose_items = ["Add vehicle to the Fleet", "Driving with the vehicle", "Refueling of the vehicle","Current status of the Fleet", "Exit"]
    print("\nWelcome in the Fleet management:")
    for i, choice in enumerate(choose_items, 1):
        print(f"{i}. {choice}")
    while True:
        try:
            choice = int(input("Please select from the menu (1-5): ").strip())
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice, please try again!")
        except ValueError:
            print("Please add a number between 1-5!")


def main():
    my_fleet = Fleet()
    print("\nWelcome in the Fleet management:")

    while True:
        user_choice = choose_menu()

        if user_choice == 1: # add a new car
            print("\n--- Add new car ---")
            brand = input("Add a car brand (example:'Ferrari'): ").strip()
            model = input(f"Add the {brand}'s model (example:'SF90'): ").strip()

            while True:
                try:
                    year = int(input("Add the manufacturing year (example: 2025): ").strip()) #check the entered value is number or not
                    break
                except ValueError:
                    print("Please enter number in year format(example: 2025)") #if not number the entered value text and add again

            new_car = Car(brand, model, year)
            my_fleet.add_vehicle(new_car)

        elif user_choice == 2: #select the vehicle to drive
            if not my_fleet.vehicles:
                print("No cars in the fleet! Add one first.")
                continue

            my_fleet.current_status()
            car_idx = int(input("Enter the ID of the vehicle what do you want to drive: ")) - 1
            if 0 <= car_idx < len(my_fleet.vehicles):
                km = float(input("Enter distance what do you want to drive (km): "))
                my_fleet.vehicles[car_idx].drive(km)
            else:
                print("Invalid car ID!")

        elif user_choice == 3:
            if not my_fleet.vehicles:
                print("No cars in the fleet!")
                continue

            my_fleet.current_status()
            car_idx = int(input("Enter the ID of the vehicle to refuel: ")) - 1
            if 0 <= car_idx < len(my_fleet.vehicles):
                amount = float(input("Enter amount to refuel in litre(s): "))
                my_fleet.vehicles[car_idx].refueling(amount)
            else:
                print("The ID of the vehicle is not avalible, please try again!")

        elif user_choice == 4:
            my_fleet.current_status()

        elif user_choice == 5:
            print("See you!")
            break


if __name__ == "__main__":
    main()