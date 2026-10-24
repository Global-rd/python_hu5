from car_fleet_mgr import Car, Fleet


def main():
    car_1 = Car("Opel", "Corsa", 2020, "DFG321")
    car_2 = Car("Skoda", "Octavia", 2019, "KJL895")
    car_3 = Car("Toyota", "Corolla", 2021, "NEV632")
    car_4 = Car("Opel", "Adam", 2024, "HGU655")
    car_5 = Car("Tesla", "Flying", 2026, "XXX111")
    car_6 = Car("Renault", "Clio", 2021, "NNM225")

    # Vezetés és tankolás
    car_1.drive(400)
    car_2.drive(500)

    car_2.refuel(20)
    car_1.refuel(10)

    # Flotta létrehozása
    fleet_car = Fleet()

    fleet_car.add_car(car_1)
    fleet_car.add_car(car_2)
    fleet_car.add_car(car_3)
    fleet_car.add_car(car_4)
    fleet_car.add_car(car_5)
    fleet_car.add_car(car_6)

    # Autó törlése rendszám alapján
    fleet_car.remove_car("NEV632")

    # Autók listázása
    fleet_car.list_car()

    # Teljes futásteljesítmény
    sum_km = fleet_car.sum_mileage_car()

if __name__ == "__main__":
    main()