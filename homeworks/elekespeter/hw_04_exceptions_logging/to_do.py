import logging
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. FÁJLOK HELYE
# ---------------------------------------------------------------------------
# A __file__ ennek a .py fájlnak az elérési útja, a .parent a mappája.
# Így a tasks.txt és a to_do.log mindig a to_do.py mellé kerül,
# bárhonnan is indítod a programot.
BASE_DIR = Path(__file__).parent
TASKS_FILE = BASE_DIR / "tasks.txt"
LOG_FILE = BASE_DIR / "to_do.log"

# ---------------------------------------------------------------------------
# 2. LOGGING BEÁLLÍTÁSA (lesson_08/logging_basics.py alapján)
# ---------------------------------------------------------------------------
# Handler: hova menjen a log. Formatter: hogyan nézzen ki.
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.DEBUG)    # a fájlba minden bekerül
stream_handler.setLevel(logging.INFO)   # a konzolra az INFO és afölötti szintek

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


# ---------------------------------------------------------------------------
# 3. AZ 5 FÜGGVÉNY
# ---------------------------------------------------------------------------

def read_tasks(file_path):
    """
    Beolvassa a feladatokat a fájlból, és listaként adja vissza.
    Ha a fájl még nem létezik, üres listával tér vissza.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file if line.strip()]
        logger.info(f"{len(tasks)} feladat beolvasva: {file_path.name}")
        return tasks
    except FileNotFoundError:
        logger.warning(f"A {file_path.name} fájl még nem létezik, üres listával indulunk.")
        return []
    except OSError as e:
        logger.error(f"Nem sikerült beolvasni a fájlt: {e}")
        return []


def write_tasks(file_path, tasks):
    """
    Felülírja a fájlt az aktuális feladatlistával (soronként egy feladat).
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task}\n")
        logger.info(f"{len(tasks)} feladat elmentve: {file_path.name}")
    except OSError as e:
        logger.exception(f"Nem sikerült menteni a fájlt: {e}")


def view_tasks(tasks):
    """
    Kiírja a feladatokat sorszámmal együtt.
    """
    if not tasks:
        print("Nincs még egyetlen feladat sem.")
        return

    print("\nFeladatok:")
    for number, task in enumerate(tasks, 1):
        print(f"{number}. {task}")


def add_task(tasks, task):
    """
    Hozzáad egy új feladatot a listához.
    """
    task = task.strip()
    if not task:
        logger.warning("Üres feladatot nem lehet hozzáadni.")
        return

    tasks.append(task)
    logger.info(f"Feladat hozzáadva: {task}")


def remove_task(tasks, task_number):
    """
    Törli a megadott sorszámú feladatot (a sorszám 1-től indul).
    """
    if task_number < 1 or task_number > len(tasks):
        logger.warning(f"Nincs {task_number}. sorszámú feladat.")
        return

    removed = tasks.pop(task_number - 1)
    logger.info(f"Feladat törölve: {removed}")


# ---------------------------------------------------------------------------
# 4. MENÜ
# ---------------------------------------------------------------------------

def display_menu():
    """
    Kiírja a választható menüpontokat.
    """
    print("\n----- Feladatkezelő -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


# ---------------------------------------------------------------------------
# 5. FŐPROGRAM
# ---------------------------------------------------------------------------

def main():
    logger.info("A program elindult.")
    tasks = read_tasks(TASKS_FILE)   # olvasás automatikusan, induláskor

    while True:
        display_menu()
        choice = input("Válassz egy menüpontot (1-4): ").strip()

        if choice not in ["1", "2", "3", "4"]:
            logger.warning(f"Érvénytelen menüpont: {choice!r}")
            continue

        if choice == "1":
            new_task = input("Az új feladat: ")
            add_task(tasks, new_task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            if not tasks:
                continue
            try:
                number = int(input("Hányadik feladatot töröljem? "))
            except ValueError:
                logger.warning("A sorszámnak egész számnak kell lennie.")
                continue
            remove_task(tasks, number)
        else:
            write_tasks(TASKS_FILE, tasks)   # mentés csak kilépéskor
            logger.info("A program leállt.")
            break


main()
