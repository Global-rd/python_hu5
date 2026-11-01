"""
Feladatkezelő alkalmazás
● Definiálj 5 függvényt a következőkre: feladatok olvasása, feladatok 
írása, feladatok megjelenítése, egy feladat hozzáadása, egy feladat 
törlése 
● Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges 
opciókat: 
1. Add Task 
2. View Tasks 
3. Remove Task 
4. Exit 
Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok 
közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt. 
A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! Ha az 1-es 
vagy 3-as opciót választja, mindkét esetben paramétert kell átadnod a 
megfelelő függvénynek. “Exit”-re lépjen ki a program. 
Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd a 
logging module-t. Egyszerre logolj a konzolra és egy .log file-ba. A .txt file 
legyen része a pull request-nek.
"""


import logging
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.txt")
LOG_FILE = Path(__file__).with_name("app.log")

# Naplózás a konzolra és fájlba
logger = logging.getLogger("task_manager")
logger.setLevel(logging.INFO)
logger.handlers.clear()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Az öt alapfüggvény

def read_tasks():
    """Feladatok beolvasása."""
    try:
        with TASKS_FILE.open("r") as file:
            tasks = [line.rstrip("\n") for line in file if line.strip()]
        logger.info("%d feladat beolvasva.", len(tasks))
        return tasks
    except FileNotFoundError:
        logger.warning("A tasks.txt nem található.")
        return []
    except OSError:
        logger.exception("Hiba a fájl olvasásakor.")
        return []


def write_tasks(tasks):
    """Feladatok mentése a fájlba."""
    try:
        with TASKS_FILE.open("w") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info("%d feladat elmentve.", len(tasks))
    except OSError:
        logger.exception("Hiba a fájl írásakor.")
        print("Hiba történt a mentés során.")


def view_tasks(tasks):
    """Feladatok megjelenítése."""
    if not tasks:
        print("\nNincsenek feladatok.")
        return

    print("\n--- Feladatok ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks, task):
    """Új feladat hozzáadása."""
    task = task.strip()
    if not task:
        print("A feladat nem lehet üres.")
        return

    tasks.append(task)
    logger.info("Feladat hozzáadva: %s", task)
    print(f'Feladat hozzáadva: "{task}"')


def remove_task(tasks, task_number):
    """Feladat törlése sorszám alapján."""
    if not tasks:
        print("Nincs törölhető feladat.")
        return

    # Hibakezelés

    try:
        index = int(task_number) - 1
        if index < 0 or index >= len(tasks):
            print("Érvénytelen sorszám.")
            return

        removed = tasks.pop(index)
        logger.info("Feladat törölve: %s", removed)
        print(f'Törölt feladat: "{removed}"')
    except ValueError:
        print("A sorszámnak egész számnak kell lennie.")

# Menü megjelenítése
        
def display_menu():
    """Menüpontok megjelenítése."""
    print("\n===== Feladatkezelő =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    # Automatikus beolvasás induláskor
    tasks = read_tasks()

    while True:
        display_menu()
        choice = input("Válassz egy opciót (1-4): ").strip()

        # Input ellenőrzése

        if choice not in {"1", "2", "3", "4"}:
            print("Érvénytelen választás! 1, 2, 3 vagy 4 adható meg.")
            logger.warning("Érvénytelen választás: %s", choice)
            continue

        if choice == "1":
            task = input("Add meg az új feladatot: ")
            add_task(tasks, task)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                number = input("Melyik feladatot töröljük? Sorszám: ")
                remove_task(tasks, number)

        elif choice == "4":
            # Mentés kizárólag kilépéskor
            write_tasks(tasks)
            print("Kilépés. Viszlát!")
            logger.info("A program befejeződött.")
            break


if __name__ == "__main__":
    main()
