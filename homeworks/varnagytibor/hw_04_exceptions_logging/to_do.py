import logging
import os

#a feladatlista és a log file a program mellett legyen, bárhonnan is indítjuk
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.txt")
LOG_FILE = os.path.join(BASE_DIR, "to_do.log")

#logging beállítása: egyszerre a konzolra ÉS egy .log file-ba írunk
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, encoding="utf-8")
    ]
)


def read_tasks(file_path):
    """Beolvassa a feladatokat a file-ból, és listaként visszaadja."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            #minden sor egy feladat, az üres sorokat kihagyjuk
            tasks = [line.strip() for line in file if line.strip()]
        logging.info(f"{len(tasks)} task(s) loaded from {os.path.basename(file_path)}.")
        return tasks
    except FileNotFoundError:
        #ha még nincs file (első indítás), üres listával indulunk
        logging.warning(f"{os.path.basename(file_path)} not found, starting with an empty list.")
        return []
    except OSError as error:
        logging.error(f"Could not read the tasks file: {error}")
        return []


def write_tasks(file_path, tasks):
    """Felülírja a file-t a memóriában lévő feladatlistával."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        logging.info(f"{len(tasks)} task(s) saved to {os.path.basename(file_path)}.")
    except OSError as error:
        logging.error(f"Could not write the tasks file: {error}")


def display_tasks(tasks):
    """Kiírja a feladatokat sorszámozva."""
    if not tasks:
        print("There are no tasks yet.")
        return
    print("Your tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task(tasks, task):
    """Hozzáad egy feladatot a listához."""
    tasks.append(task)
    logging.info(f"Task added: {task}")


def remove_task(tasks, task_number):
    """Törli a megadott sorszámú feladatot (a sorszám 1-től indul)."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        logging.info(f"Task removed: {removed}")
    else:
        logging.warning(f"Invalid task number: {task_number}")


def display_menu():
    """Kiírja a menüpontokat."""
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


#indításkor automatikusan beolvassuk a feladatokat a memóriába (egy listába)
tasks = read_tasks(TASKS_FILE)

#folyamatosan kérjük a menüpontot, amíg a felhasználó ki nem lép
while True:
    display_menu()
    choice = input("Choose an option (1-4): ").strip()

    #csak 1, 2, 3 vagy 4 fogadható el
    if choice not in ["1", "2", "3", "4"]:
        print("Error: please enter 1, 2, 3 or 4!")
        logging.warning(f"Invalid menu choice: {choice}")
        continue

    if choice == "1":
        task = input("New task: ").strip()
        if task:
            #paraméterként adjuk át az új feladatot
            add_task(tasks, task)
        else:
            print("Error: the task cannot be empty!")
    elif choice == "2":
        display_tasks(tasks)
    elif choice == "3":
        display_tasks(tasks)
        try:
            #paraméterként adjuk át a törlendő feladat sorszámát
            task_number = int(input("Number of the task to remove: "))
            remove_task(tasks, task_number)
        except ValueError:
            print("Error: please enter a number!")
            logging.warning("Remove Task: the input was not a number.")
    else:
        #Exit: csak most írjuk ki a file-ba a módosított listát, majd kilépünk
        write_tasks(TASKS_FILE, tasks)
        logging.info("Program finished.")
        break
