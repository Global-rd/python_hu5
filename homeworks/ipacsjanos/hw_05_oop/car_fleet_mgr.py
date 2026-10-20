# ==========================================
# CAR OSZTÁLY DEFINÍCIÓJA
# ==========================================
class Car:
    """Egy autót reprezentáló osztály."""

    def __init__(self, brand, model, year):
        """Konstruktor, amely beállítja az autó alapvető tulajdonságait."""
        self.brand = brand          # Autó márkája (pl. Ford)
        self.model = model          # Autó modellje (pl. Focus)
        self.year = year            # Gyártási éve
        self.mileage = 0            # Kilométeróra állása (induló érték: 0)
        self.fuel_level = 100       # Üzemanyag-szint százalékban (induló érték: 100%)

    def drive(self, kilometers):
        """Vezetés metódus: növeli a kilométert és csökkenti az üzemanyagot (0.1% / km)."""
        # Kiszámoljuk, hogy a kért távolsághoz mennyi üzemanyag kellene
        needed_fuel = kilometers * 0.1
        
        # Ellenőrizzük, hogy van-e elég üzemanyag
        if self.fuel_level >= needed_fuel:
            self.mileage += kilometers       # Növeljük a megtett kilométerek számát
            self.fuel_level -= needed_fuel   # Csökkentjük az üzemanyag-szintet
            print(f"[DRIVE] Sikeresen levezettél {kilometers} km-t a(z) {self.brand} {self.model} autóval.")
        else:
            # Ha nincs elég üzemanyag, kiszámoljuk, maximum hány km-t tud megtenni a jelenlegi szinttel
            max_km = self.fuel_level / 0.1
            self.mileage += max_km           # Megteszi a maximális távolságot
            self.fuel_level = 0              # Teljesen kiürül a tank
            print(f"[DRIVE] Nincs elég üzemanyag {kilometers} km-re! Csak {max_km:.1f} km-t haladtál, a tank kiürült.")

    def refuel(self, amount):
        """Tankolás metódus: növeli az üzemanyag-szintet, figyelve a 100%-os limitre."""
        if amount < 0:
            print("[REFUEL] Hiba: Negatív mennyiséget nem lehet tankolni!")
            return

        if self.fuel_level + amount > 100:
            self.fuel_level = 100  # Nem engedjük 100% fölé menni a tankot
            print(f"[REFUEL] A(z) {self.brand} tankja teljesen tele lett (100%).")
        else:
            self.fuel_level += amount  # Hozzáadjuk a tankolt mennyiséget
            print(f"[REFUEL] Tankolva {amount}%. Jelenlegi szint: {self.fuel_level}%.")

    def display_status(self):
        """Kiprinteli az autó aktuális adatait."""
        print(f" -> {self.brand} {self.model} ({self.year}) | Km: {self.mileage} km | Üzemanyag: {self.fuel_level}%")


# ==========================================
# FLEET (FLOTTA) OSZTÁLY DEFINÍCIÓJA
# ==========================================
class Fleet:
    """Autók flottáját kezelő osztály."""

    def __init__(self):
        """Konstruktor, ami létrehoz egy üres listát az autók tárolására."""
        self.cars = []  # Ebben a listában tároljuk majd a Car objektumokat

    def add_car(self, car):
        """Új Car objektum hozzáadása a flottához."""
        self.cars.append(car)
        print(f"[FLEET] {car.brand} {car.model} hozzáadva a flottához.")

    def remove_car(self, car):
        """Egy Car objektum eltávolítása a flottából, ha benne van."""
        if car in self.cars:
            self.cars.remove(car)
            print(f"[FLEET] {car.brand} {car.model} eltávolítva a flottából.")
        else:
            print(f"[FLEET] Hiba: A(z) {car.brand} {car.model} nem található a flottában.")

    def get_total_mileage(self):
        """Összesíti a flottában lévő autók kilométeróra állásait."""
        total = 0
        for car in self.cars:
            total += car.mileage  # Összeadjuk minden autó saját mileage értékét
        return total

    def display_fleet_status(self):
        """Megjeleníti a flotta teljes állapotát."""
        print("\n--- FLOTTA ÁLLAPOT JELENTÉS ---")
        if not self.cars:
            print("A flotta jelenleg üres.")
        else:
            for car in self.cars:
                car.display_status()  # Meghívjuk az autó saját státusz-kiíró metódusát
            print(f"Flotta összesített futásteljesítménye: {self.get_total_mileage()} km")
        print("--------------------------------\n")


# ==========================================
# FŐPROGRAM - TESZTELÉS ÉS MŰVELETEK
# ==========================================
if __name__ == "__main__":
    # 1. Hozunk létre néhány Car objektumot (példányt)
    car1 = Car("Ford", "Focus", 2018)
    car2 = Car("Toyota", "Yaris", 2021)
    car3 = Car("BMW", "320i", 2015)

    # 2. Létrehozzuk a flottát és hozzáadjuk az autókat
    my_fleet = Fleet()
    my_fleet.add_car(car1)
    my_fleet.add_car(car2)
    my_fleet.add_car(car3)

    # Megnézzük a kezdő állapotot
    my_fleet.display_fleet_status()

    # 3. Műveletek végrehajtása (Vezetés és Tankolás)
    print("--- Műveletek indítása ---")
    car1.drive(300)   # 300 km vezetés -> 30% üzemanyag fogy, marad 70%
    car2.drive(1200)  # 1200 km-t akarunk vezeti -> nincs elég üzemanyag (csak 1000 km-re elég)
    
    # Státusz ellenőrzése a műveletek után
    my_fleet.display_fleet_status()

    # Tankolás tesztelése
    car2.refuel(50)   # Tankolunk 50%-ot a kiürült Toyotába
    car1.refuel(40)   # A Fordba 40%-ot tankolunk (70+40=110 lenne, de lekorlátoz 100-ra)

    # Vezetés tankolás után
    car2.drive(200)   # Most már tud menni a Toyota

    # 4. Egy autó eltávolítása a flottából tesztelésképp
    print("\n--- Flotta módosítása ---")
    my_fleet.remove_car(car3)

    # Végső összesített adatok megjelenítése
    my_fleet.display_fleet_status()
