import os
from pathlib import Path
import logging

print(os.getcwd())

#Function-ök készítése az alábbi feladatokkal:
#feladatok olvasása
#feladatok írása
#egy feladat hozzáadása
#egy feladat törlése
#display_menu, ami kiprinteli az Add Task, View Task, Remove Task, Exit 
#kérjük be. hogy mit szeretne a felhasználó csinálni és a megadott feltételnek megfelelő függvényt hívjuk be

file_path = Path("homeworks")/"bretankrisztina"/"hw_04_exceptions_logging"/"tasks.txt"

#logging:
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", encoding="utf-8")

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

#Feladatok olvasása fájlból
def read_tasks(file_path):
    """
    Reading tasks from a .txt file.
    """
    try:
        with open(file_path, "r", encoding= "utf-8") as file:
            tasks = file.readlines()
            tasks = [line.strip() for line in tasks]
        return tasks
    
    except FileNotFoundError as e:
        logging.warning(f"Task file is not found. {e}")
        return[]

    except PermissionError as e:
        logging.warning(f"You do not have permission, please turn to the IT department. {e}")

    except ValueError as e:
        logging.warning(f"The file is wrong extension. {e}")

#Feladat írása
def write_tasks(tasks):
    """
    Writing a tasks to .txt file.
    """
    try:
        with open(file_path, "w", encoding= "utf-8") as file: 
            for task in tasks:
                file.write(task +"\n")
        return True
    
    except OSError as e:
        logging.error(f"No space left in file. {e}")

#Feladat hozzáadása, ha a szóközök eltávolítása után marad még valamilyen szöveg
def add_task(tasks, task):
    """
    Appending tasks- writing to .txt file with Exit option.
    """
    if task.strip() != "": 
        tasks.append(task.strip("\n"))
        logging.info(f"Task added: {task}")
        print("Task adding is successfully.")
    else:
        print("Task cannot be empty")

#Feladat törlése
def remove_task(tasks, task_number: int):
    """
    Remove tasks from the .txt file with Exit option.
    """
    if task_number >= 0:
        removed_task = tasks.pop(task_number - 1)
        logging.info(f"Task removed: {removed_task}")
        print("Task removing is successfully.")
    elif task_number > len(tasks):
        print("Invalid task number.")

#Feladat megjelenítése
def view_task(tasks):
    """
    Display tasks to the users demand.
    """
    if not tasks:
        print("No tasks available")
    else:
        print("Tasks:")
        for id, task in enumerate(tasks, 1):
            print(f"{id}. {task.strip("\n")}")

def display_tasks_menu():
    """
    Display menu to users
    """
    print("\nTask menu:")
    print("1. Add Task"),
    print("2. View Tasks"),
    print("3. Remove Task"),
    print("4. Exit")

# Főprogram
def main():

#feladatok fájlból beolvasása listába 
    tasks = read_tasks(file_path)

    while True:

        display_tasks_menu()
        
        try:
            options = int(input("Please choose an option from the list: "))
            
        except ValueError as e:
            logging.warning(f"Please enter a valid number from the list. {e}")
            continue

#Új feladatot lehet megadni
        if options == 1:
            task = input("Enter a new task: ")
            add_task(tasks, task)

#Megtekinteni a lehetőségeket        
        elif options == 2:
            view_task(tasks)

#Törölni kell a kiválasztott sort
        elif options == 3:
            view_task(tasks)
            if tasks:
                task_number = int(input("Enter a removing task number: "))
                remove_task(tasks, task_number)
            else:
                "There is not a good option, please choose an other one from the list."

#Ki kell lépni a programból .txt mentéssel
        elif options == 4:
            if write_tasks(tasks):
                print("The .txt file is saved")
                break
            else:
                print("Could not save the tasks, please try it again.")
        else: 
            print("Invalid option, please choose one from the list. ")
main()