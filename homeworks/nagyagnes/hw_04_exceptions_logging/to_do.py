# --- feladatkezelő alkalmazás ---
 
import logging
from pathlib import Path
 

BASE_DIR = Path(__file__).parent # a fájlok a to_do.py mellé kerülnek (ugyanebben a mappában hozza létre a fájlokat9
TASKS_FILE = BASE_DIR / "tasks.txt"
LOG_FILE = BASE_DIR / "to_do.log"
 

file_handler = logging.FileHandler(LOG_FILE) # logging beállítása: egyszerre konzolra és egy .log fájlba
stream_handler = logging.StreamHandler()
 
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
 
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
 
file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.INFO)
 
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
 
logger.setLevel(logging.DEBUG)
 
def read_tasks(file_path):
    """
    1 Feladatok olvasása
    """
 
    tasks = []
 
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                task = line.strip()
                if task:
                    tasks.append(task)
        logger.info(f"Loaded {len(tasks)} task(s) from {file_path.name}")
    except FileNotFoundError:
        logger.warning(f"No {file_path.name} yet, so we're starting with an empty list.")
    except Exception as e:
        logger.exception(f"Something went wrong while reading the file: {e}")
    return tasks
 
 
def write_tasks(file_path, tasks):
    """
    2 Feladatok írása
    """
    try:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info(f"Saved {len(tasks)} task(s) to {file_path.name}")
    except Exception as e:
        logger.exception(f"Something went wrong while saving the file: {e}")
 
 
def display_tasks(tasks):
    """
    3 Feladatok megjelenítése
    """
    if not tasks:
        print("Your list is empty, nothing to do!")
        return
 
    print("\nHere's your list:")
    for number, task in enumerate(tasks, 1):
        print(f"{number}. {task}")
 
 
def add_task(tasks, task):
    """
    4 Feladat hozzáadása
    """
    tasks.append(task)
    logger.info(f"New task added: {task}")
 
 
def remove_task(tasks, task_number):
    """
    5 Feladat törlése a sorszáma alapján
    """
    if task_number < 1 or task_number > len(tasks):
        logger.warning(f"There's no task number {task_number}")
        return
 
    task = tasks[task_number - 1]
    tasks.remove(task)
    logger.info(f"Task removed: {task}")
 
 
def display_menu():
    """
    Lehetséges opciók kiprintelése
    """
    print("\n--- My To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
 
 
def main():
    tasks = read_tasks(TASKS_FILE)  # beolvasás a program indításakor
 
    while True:
        display_menu()
        choice = input("What would you like to do? (1-4): ").strip()
 
        if choice not in ["1", "2", "3", "4"]:
            logger.warning(f"Unknown menu option: {choice}")
            print("That's not an option. Just pick 1, 2, 3 or 4.")
            continue
 
        if choice == "1":
            task = input("What's the new task? ").strip()
            if task:
                add_task(tasks, task)
            else:
                print("Looks like you didn't type anything.")
 
        elif choice == "2":
            display_tasks(tasks)
 
        elif choice == "3":
            display_tasks(tasks)
            if not tasks:
                continue
            try:
                task_number = int(input("Which one would you like to remove? "))
                remove_task(tasks, task_number)
            except ValueError as e:
                logger.warning(f"That wasn't a number: {e}")
                print("That doesn't look like a number. Try again!")
 
        elif choice == "4":
            write_tasks(TASKS_FILE, tasks)  # fájlba írás csak a program befejezésekor
            logger.info("See you next time!")
            break
 
 
main()
