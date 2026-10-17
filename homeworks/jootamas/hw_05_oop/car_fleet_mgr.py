# Car() és Fleet() mehetne külön modulba és import, itt pedig csak a main(), de ez nem volt feladat, ezért maradtak itt egyben

class Car:
  def __init__(self, brand:str, model:str, year:int, mileage:int, fuel_level:float):
    # Egy konstruktor, amely beállítja a fenti attribútumokat.
    self.brand = brand
    self.model = model
    self.year = year
    self.mileage = mileage
    self.fuel_level = fuel_level # percent

  def drive(self, km:int=0):
    """
    Egy drive() metódus, amely adott számú kilométerrel növeli a
    kilométeróra állását, és csökkenti az üzemanyag-szintet (tételezzük fel,
    hogy 0.1% üzemanyag fogy megtett kilométerenként). A drive()
    metódus csak annyit km-et engedjen vezetni, amennyire elegendő
    üzemanyag van.
    """
    if not(isinstance(km, int)) or km <= 0:
      raise ValueError(f"{self.brand} {self.model}: A megadott km csak pozitív egész szám lehet")
    if self.fuel_level < km * 0.1:
      raise ValueError(f"{self.brand} {self.model}: Nincs elég üzemanyag a megadott km megtételéhez")
    self.mileage += km
    self.fuel_level -= km * 0.1

  def refuel(self, percent:int=0):
    # Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel. Figyelj a limitekre.
    if not(isinstance(percent, int)) or percent <= 0:
      raise ValueError(f"{self.brand} {self.model}: A tankolt mennyiség csak pozitív egész szám lehet")
    if percent > 100:
      raise ValueError(f"{self.brand} {self.model}: A tankolt mennyiség nem lehet 100-nál több")
    if percent + self.fuel_level > 100:
      raise ValueError(f"{self.brand} {self.model}: A tankolt mennyiség nem fér a tankba, a tank jelenlegi szintje {self.fuel_level}%")
    self.fuel_level += percent

# Készíts egy Fleet osztályt, amely kezeli a Car objektumokat
class Fleet:
  # Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
  cars = []
  def __init__(self):
    pass
  def add_car(self, *new_cars):
    # Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából.
    for i, car in enumerate(new_cars, 1):
      if not(isinstance(car, Car)):
        raise ValueError(f"A(z) {i}. hozzáadott elem nem egy Car példány")
      self.cars.append(car)
  def remove_car(self, removed_car):
    # Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából.
    if not(isinstance(removed_car, Car)):
      raise ValueError(f"Sikertelen törlés, a megadott objektum nem egy Car példány")
    for car in self.cars:
      if car == removed_car:
        self.cars.remove(removed_car)
        break
  def sum_mileage(self):
    # Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét.
    sum = 0
    for car in self.cars:
      sum += car.mileage
    return sum

def main():
  """
  Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts
  végre néhány műveletet (vezetés, tankolás), jelenítsd meg az autók
  állapotát és a flotta összesítő adatait.
  """
  fleet = Fleet()

  car_1 = Car(brand="Opel", model="Astra", year=2010, mileage=1010, fuel_level=90)
  car_2 = Car(brand="Opel", model="Corsa", year=2012, mileage=2222, fuel_level=80)
  car_3 = Car(brand="Volkswagen", model="Polo", year=2005, mileage=3333, fuel_level=70)
  car_4 = Car(brand="Citroen", model="C3", year=2014, mileage=5050, fuel_level=60)
  car_5 = Car(brand="Toyota", model="Corolla", year=2002, mileage=6080, fuel_level=50)
  # ha ezt is hozzaadjuk, akkor hibauzenet, mert nem egy Car peldany
  # car_6 = "x"

  try:
    fleet.add_car(car_1, car_2, car_3, car_4, car_5)
  except Exception as e:
    print(e)
  else:
    print("Az autók sikeresen hozzáadva")

  print("----------")

  try:
    # DRIVE
    fleet.cars[0].drive(53) # megyunk egyet az Astraval
    fleet.cars[1].drive(108) # megyunk egyet a Corsaval

    # raise, a megtett km csak pozitiv egesz lehet
    # fleet.cars[0].drive(-1)

    # raise, nincs eleg uzemanyag
    # fleet.cars[0].drive(5000000)

    # REFUEL
    fleet.cars[2].refuel(3) # tankolunk a Polo-ba
    fleet.cars[3].refuel(8) # tankolunk a C3-ba

    # raise, 200%-nyit nem lehet tankolni
    # fleet.cars[3].refuel(200)

    # raise, ennyi nem fer a tankba
    # fleet.cars[3].refuel(90)

    # REMOVE
    # a Toyotat toroljuk
    fleet.remove_car(fleet.cars[4])

    # raise, mert ertelmetlen, hogy az x-et toroljuk a flottabol
    # fleet.remove_car("x")

  except Exception as e:
    print(e)
  else:
    print("A műveletek sikeresen felvezetve az adatbázisba")

  print("----------")
  for car in fleet.cars:
    print(f"{car.brand} {car.model} ({car.year}), km óra állása: {car.mileage}, üzemanyagszint: {car.fuel_level:.1f}")

  print("----------")
  print(f"A flotta összes autójának összes megtett kilométere: {fleet.sum_mileage()}")

main()
