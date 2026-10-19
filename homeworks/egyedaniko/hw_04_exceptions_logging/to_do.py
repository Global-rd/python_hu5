"""
Simple To Do Application
"""

import logging

# Logging beállítása konzolra és fájlba
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("todo.log"),
        logging.StreamHandler()
    ]
)

TASK_FILE = "tasks.txt"


def read_tasks():
    """Feladatok beolvasása fájlból."""

    try:

        # Fájl megnyitása olvasásra
        with open(TASK_FILE, "r") as file:

            # Sorok beolvasása listába
            tasks = [line.strip() for line in file.readlines()]

            logging.info("Tasks loaded successfully.")

            return tasks

    except FileNotFoundError:

        # Ha még nem létezik a fájl, üres listával indulunk
        logging.warning("tasks.txt not found.")

        return []

    except Exception as e:

        logging.error(f"Error while reading file: {e}")

        return []


def write_tasks(tasks):
    """Feladatok mentése fájlba."""

    try:

        # Fájl megnyitása felülírásra
        with open(TASK_FILE, "w") as file:

            # Minden feladat külön sorba kerül
            for task in tasks:
                file.write(task + "\n")

        logging.info("Tasks saved successfully.")

    except Exception as e:

        logging.error(f"Error while saving tasks: {e}")


def display_tasks(tasks):
    """Feladatok megjelenítése."""

    if len(tasks) == 0:

        print("\nNincs egyetlen feladat sem.")

        return

    print("\nFeladatok:")

    # Számozott lista kiírása
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks, task):
    """Új feladat hozzáadása."""

    # Új feladat hozzáadása a listához
    tasks.append(task)

    logging.info(f"Task added: {task}")


def remove_task(tasks, task_number):
    """Feladat törlése."""

    try:

        # A kiválasztott feladat törlése
        removed_task = tasks.pop(task_number - 1)

        logging.info(f"Task removed: {removed_task}")

    except IndexError:

        print("Érvénytelen sorszám.")

        logging.error("Invalid task number.")


def display_menu():
    """Menü megjelenítése."""

    print("\n===== TO DO MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


# Feladatok automatikus betöltése indításkor
tasks = read_tasks()

# Fő programciklus
while True:

    display_menu()

    choice = input("Choose an option (1-4): ")

    # Menüpont ellenőrzése
    if choice not in ["1", "2", "3", "4"]:

        print("Invalid menu option!")

        continue

    if choice == "1":

        # Új feladat bekérése
        task = input("Enter task: ")

        add_task(tasks, task)

    elif choice == "2":

        # Feladatok megjelenítése
        display_tasks(tasks)

    elif choice == "3":

        # Feladatok listázása törlés előtt
        display_tasks(tasks)

        try:

            task_number = int(
                input("Enter task number to remove: ")
            )

            remove_task(tasks, task_number)

        except ValueError:

            print("Kérlek számot adj meg.")

    elif choice == "4":

        # Kilépés előtt mentés fájlba
        write_tasks(tasks)

        print("Tasks saved.")
        print("Goodbye!")

        logging.info("Program exited.")

        break