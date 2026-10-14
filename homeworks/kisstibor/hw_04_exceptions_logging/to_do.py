"""
HÁZI FELADAT 04: To-Do lista kezelő program
hw_04_exceptions_logging/to_do.py

Feladatok hozzáadása, listázása és törlése.
A feladatok a program mappájában található tasks.txt fájlba kerülnek mentésre.
Naplózás a program mappájában található to_do.log fájlba történik.
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# A Path a Windows és Linux útvonal-elválasztóit is automatikusan kezeli.
PROGRAM_FOLDER = Path(__file__).parent
TASKS_FILE = PROGRAM_FOLDER / "tasks.txt"
LOG_FILE = PROGRAM_FOLDER / "to_do.log"


def read_tasks():
    """Beolvassa a TASKS_FILE fájlban elmentett feladatokat egy listába."""
    tasks = []

    try:
        # UTF-8 kódolással a magyar ékezetek is helyesen olvashatók be.
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # A sorvégeket levágjuk, hogy tiszta feladatnevek kerüljenek a listába.
        for line in lines:
            task = line.strip()
            if task != "":
                tasks.append(task)

        logger.info(f"A feladatok beolvasása '{TASKS_FILE}' fájlból sikerült.")
    except FileNotFoundError:
        # Ha még nincs mentés, a program üres feladatlistával indul.
        logger.warning(f"A '{TASKS_FILE}' nem létezik. A feladat lista üres.")
    except OSError as error:
        logger.exception("Hiba történt a feladatok beolvasásakor: %s", error)
        raise

    return tasks


def write_tasks(tasks):
    """Kiírja a teljes feladatlistát a fájlba."""
    try:
        # Ugyanazzal a kódolással mentünk, amellyel be is olvassuk a fájlt.
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")

        logger.info(f"A feladatok mentése '{TASKS_FILE}' fájlba sikerült.")
    except OSError as error:
        logger.exception("Hiba történt a feladatok mentésekor a(z) '%s' fájlba: %s", TASKS_FILE, error)
        raise


def display_tasks(tasks):
    """Sorszámozva megjeleníti a feladatlistát."""
    if len(tasks) == 0:
        print("Nincsenek feladatok.")
    else:
        print("\n  ╔═ Feladatok (Tasks) ════════════════════════════════════════")
        for number, task in enumerate(tasks, 1):
            print(f"  ║ {number}. {task}")
        print("  ╚════════════════════════════════════════════════════════════")    


def add_task(tasks):
    """Bekér egy feladatot, és hozzáadja a memóriabeli listához."""
    task = input("Add meg az új feladatot: ").strip()

    if task == "":
        print("A feladat nem lehet üres.")
        logger.warning("Üres feladatot nem lehet hozzáadni.")
    else:
        tasks.append(task)
        print("A feladat hozzáadása sikerült.")
        logger.info("Új feladat hozzáadva: %s", task)


def remove_task(tasks):
    """Bekéri a törlendő feladat sorszámát, majd eltávolítja a listából."""
    if len(tasks) == 0:
        print("Nincsenek törölhető feladatok.")
        return

    display_tasks(tasks)

    try:
        task_number = int(input("Add meg a törlendő feladat sorszámát: "))
    except ValueError as error:
        print("Adj meg egy érvényes egész számot.")
        logger.warning("Érvénytelen feladatsorszám: %s", error)
        return

    if task_number < 1 or task_number > len(tasks):
        print("Nincs ilyen sorszámú feladat.")
        logger.warning("A megadott sorszám nem található: %s", task_number)
    else:
        removed_task = tasks.pop(task_number - 1)
        print("A feladat törlése sikerült.")
        logger.info("Feladat törölve: %s", removed_task)


def display_menu():
    """Megjeleníti a választható menüpontokat."""
    print("\n▒▒ MENU ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒ 1. Feladat rögzítés (Add Task)       ▒")
    print("▒ 2. Feladatok listázása (List Tasks)  ▒")
    print("▒ 3. Feladat törlése (Remove Task)     ▒")
    print("▒ 4. Kilépés (Exit)                    ▒ ")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")


def setup_logging():
    """Beállítja a naplózást a konzolra és egy naplófájlba."""
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    file_handler.setLevel(logging.INFO)
    stream_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)


def main():
    """Elindítja a programot, és kezeli a menüpontok közötti választást."""
    setup_logging()

    # Induláskor beolvassuk a mentést; módosításkor csak a lista változik.
    tasks = read_tasks()

    while True:
        display_menu()
        menu_choice = input("Válassz egy menüpontot (1-4): ")

        if  menu_choice == "1":
            add_task(tasks)

        elif menu_choice == "2":
            display_tasks(tasks)

        elif menu_choice == "3":
            remove_task(tasks)
            display_tasks(tasks)

        elif menu_choice == "4":
            # A fájlba mentés kizárólag a programból való kilépéskor történik.
            write_tasks(tasks)
            print(f"A feladatok elmentve a '{TASKS_FILE}' fájlba!")
            logger.info("A program futása sikeresen befejeződött.")
            break

        else:
            print("Érvénytelen választás. 1 és 4 közötti számot adj meg.")
            logger.warning("Érvénytelen menüpont: %s", choice)


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    main()
