import logging  # Beimportáljuk a logging modult a naplózáshoz (fájlba/konzolra íráshoz)
import os  # Beimportáljuk az os modult, amivel ellenőrizni tudjuk, hogy létezik-e már a fájl

# --- LOGGING BEÁLLÍTÁSA ---
logger = logging.getLogger("ToDoLogger")  # Létrehozzuk a saját nevű naplózó objektumunkat (loggert)
logger.setLevel(logging.INFO)  # Beállítjuk a log szintet INFO-ra (minden fontos eseményt rögzítünk)

# Meghatározzuk a log üzenetek kinézetét: Időpont - Fontossági szint - Üzenet szövege
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 1. FÁJLBA LOGOLÁS BEÁLLÍTÁSA
file_handler = logging.FileHandler("todo_app.log", encoding="utf-8")  # Megadjuk a log fájl nevét és az UTF-8 kódolást
file_handler.setFormatter(formatter)  # Rákapcsoljuk a fájlkezelőre a fent megírt szövegformátumot
logger.addHandler(file_handler)  # Hozzáadjuk ezt a fájlkezelőt a fő loggerünkhöz

# 2. KONZOLRA LOGOLÁS BEÁLLÍTÁSA
console_handler = logging.StreamHandler()  # Létrehozunk egy kezelőt, ami a képernyőre (terminálba) küldi a logokat
console_handler.setFormatter(formatter)  # Erre is rákapcsoljuk ugyanazt a szövegformátumot
logger.addHandler(console_handler)  # Hozzáadjuk ezt a konzolkezelőt is a fő loggerünkhöz


# --- GLOBÁLIS VÁLTOZÓK ---
FILE_NAME = "todo_list.txt"  # Egy konstans változóban elmentjük a feladatokat tároló szöveges fájl nevét
tasks = []  # Létrehozunk egy üres listát, ebben fogjuk tárolni a feladatokat a gép memóriájában futás közben


# --- FÜGGVÉNYEK DEFINIÁLÁSA ---

def read_tasks():  # Definiáljuk a feladatok beolvasásáért felelős függvényt
    global tasks  # Jelezzük, hogy a függvényen belül a globális (fenti) 'tasks' listát akarjuk módosítani
    if not os.path.exists(FILE_NAME):  # Megnézzük az os segítségével, hogy létezik-e már a todo_list.txt fájl
        logger.info(f"A(z) {FILE_NAME} még nem létezik, üres listával indulunk.")  # Ha nem létezik, logoljuk és...
        return  # ...azonnal kilépünk a függvényből, hiszen nincs mit beolvasni

    try:  # Elindítjuk a hibakezelő blokkot az olvasáshoz
        with open(FILE_NAME, "r", encoding="utf-8") as file:  # Megnyitjuk a fájlt olvasásra ("r") UTF-8 kódolással
            # Beolvassuk az összes sort, levágjuk a láthatatlan sortöréseket (\n), és csak a nem üres sorokat tartjuk meg
            tasks = [line.strip() for line in file.readlines() if line.strip()]
        logger.info(f"Sikeresen beolvasva {len(tasks)} feladat a fájlból.")  # Logoljuk, hány darab feladatot találtunk
    except Exception as e:  # Ha bármilyen hiba történne a beolvasás alatt (pl. hibás fájlformátum)...
        logger.error(f"Hiba történt a fájl olvasása közben: {e}")  # ...akkor elkapjuk a hibát és naplózzuk a részleteit


def write_tasks():  # Definiáljuk a feladatok elmentéséért felelős függvényt
    try:  # Elindítjuk a hibakezelő blokkot az íráshoz
        with open(FILE_NAME, "w", encoding="utf-8") as file:  # Megnyitjuk a fájlt írásra ("w"), ami teljesen felülírja a régit
            for task in tasks:  # Egy 'for' ciklussal végigmegyünk a memóriában lévő 'tasks' lista összes elemén
                file.write(task + "\n")  # Beleírjuk az aktuális feladatot a fájlba, a végére egy sortörést (\n) rakva
        logger.info("A feladatok sikeresen elmentve a fájlba.")  # Ha sikerült, elmentjük a sikeres log üzenetet
    except Exception as e:  # Ha az írás közben hiba lépne fel (pl. megtelt a lemez vagy zárolt a fájl)...
        logger.error(f"Hiba történt a fájl mentése közben: {e}")  # ...akkor elkapjuk és ERROR szinten naplózzuk


def display_tasks():  # Definiáljuk a feladatok képernyőre írásáért felelős függvényt
    print("\n--- AKTUÁLIS FELADATOK ---")  # Kiírunk egy szép fejlécet a konzolra
    if not tasks:  # Megnézzük, hogy üres-e a 'tasks' lista
        print("A feladatlista jelenleg üres.")  # Ha üres, ezt külön jelezzük a felhasználónak
    else:  # Ha vannak elemek a listában...
        for index, task in enumerate(tasks, start=1):  # Az enumerate segítségével 1-től sorszámozzuk az elemeket
            print(f"{index}. {task}")  # Kiírjuk a sorszámot és magát a feladat szövegét egy f-stringgel
    print("--------------------------")  # Kiírunk egy lezáró vonalat


def add_task(new_task):  # Definiáljuk a feladat hozzáadását végző függvényt, ami vár egy 'new_task' paramétert
    if new_task.strip():  # Ellenőrizzük, hogy a beírt feladat nem csak üres szóközökből áll-e
        tasks.append(new_task.strip())  # Ha érvényes, szóközök nélkül hozzáadjuk a 'tasks' lista végére
        logger.info(f"Feladat hozzáadva: '{new_task}'")  # Sikeresen naplózzuk a feladat hozzáadását
    else:  # Ha a felhasználó semmit nem írt be, csak Entert nyomott...
        print("Hiba: Üres feladatot nem lehet hozzáadni!")  # ...kiírunk egy figyelmeztetést a képernyőre


def remove_task(task_index):  # Definiáljuk a törlés függvényt, ami megkapja a törlendő feladat sorszámát (paraméterként)
    try:  # Hibakezelést indítunk, mert a törlésnél elcsúszhat az indexelés
        actual_index = task_index - 1  # Mivel a felhasználó 1-től látja a listát, de a Python 0-tól indexel, levonunk egyet
        if 0 <= actual_index < len(tasks):  # Ellenőrizzük, hogy a kiszámolt index valóban benne van-e a lista határai között
            removed = tasks.pop(actual_index)  # A .pop() segítségével kivesszük és töröljük az adott indexű elemet
            logger.info(f"Feladat eltávolítva: '{removed}'")  # Sikeresen naplózzuk a törölt feladat nevét
        else:  # Ha olyan számot adott meg, ami nincs a listában (pl. van 3 feladat, de ő a 9-est kéri)...
            print("Hiba: Nincs ilyen sorszámú feladat a listában!")  # ...akkor jelezzük a hibát
    except TypeError:  # Ha valamilyen oknál fogva rossz adattípus érkezne az indexhez...
        print("Hiba: Érvénytelen index formátum!")  # ...akkor ezt a típusbaki hibát is kezeljük


def display_menu():  # Definiáljuk a menü kiírásáért felelős függvényt
    print("\n===== TO-DO MENÜ =====")  # Menü fejléc kiírása
    print("1. Add Task")  # 1-es opció: Új feladat hozzáadása
    print("2. View Tasks")  # 2-es opció: Feladatok megtekintése
    print("3. Remove Task")  # 3-as opció: Feladat törlése
    print("4. Exit")  # 4-es opció: Kilépés a programból
    print("======================")  # Menü lezárása


# --- FŐPROGRAM INDÍTÁSA ÉS FUTÁSI LOGIKÁJA ---

read_tasks()  # A program legelső lépéseként automatikusan meghívjuk a fájlbeolvasó függvényt

while True:  # Elindítunk egy végtelen ciklust, ami addig fut, amíg a felhasználó ki nem lép
    display_menu()  # Minden kör elején kirakjuk a képernyőre a menüpontokat
    user_input = input("Válassz egy menüpontot (1-4): ").strip()  # Bekérjük a választást, levágva a felesleges szóközöket

    if user_input == "1":  # Ha az 1-es menüpontot választotta...
        task_name = input("Írd be az új feladatot: ")  # ...bekérjük az új feladat szövegét...
        add_task(task_name)  # ...és meghívjuk az add_task függvényt, átadva neki a szöveget argumentumként

    elif user_input == "2":  # Ha a 2-es menüpontot választotta...
        display_tasks()  # ...egyszerűen meghívjuk a feladatokat listázó függvényt

    elif user_input == "3":  # Ha a 3-as menüpontot választotta...
        display_tasks()  # ...először megmutatjuk neki a listát, hogy lássa a sorszámokat
        if tasks:  # Csak akkor kérünk be sorszámot, ha egyáltalán van mit törölni a listából
            try:  # Külön try-except blokk az input számmá alakításához
                index_input = int(input("Add meg a törölni kívánt feladat sorszámát: "))  # Számmá alakítjuk a beírt szöveget
                remove_task(index_input)  # Meghívjuk a törlés függvényt, átadva neki a kapott sorszámot
            except ValueError:  # Ha a felhasználó nem számot írt be (hanem pl. azt, hogy "kutya")...
                print("Hiba: Kérlek, számot adj meg sorszámként!")  # ...akkor elkapjuk a ValueError-t és kiírjuk a hibát

    elif user_input == "4":  # Ha a 4-es menüpontot választotta (Exit)...
        logger.info("Kilépés kiválasztva. Mentés folyamatban...")  # Mentés előtti log üzenet rögzítése
        write_tasks()  # Meghívjuk a write_tasks függvényt, ami most az összes feladatot kiírja és elmenti a fájlba
        print("A program sikeresen lezárult. Szia!")  # Búcsúüzenet kiírása
        break  # A 'break' segítségével megszakítjuk a végtelen while ciklust, így a program leáll

    else:  # Ha a felhasználó nem 1, 2, 3 vagy 4 értéket gépelt be (hanem pl. 8-ast vagy betűt)...
        print("Érvénytelen választás! Kérlek, 1, 2, 3 vagy 4 számot üss be.")  # Figyelmeztetjük a helyes használatra
