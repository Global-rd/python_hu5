import logging
import os
from pathlib import Path

#logolás beállitás
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

#fájlba naplózás (file_handler)
file_handler = logging.FileHandler("to_do.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

#konzolra naplózás (stream_handler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

file_path = Path("homeworks")/"gobelgergo"/"hw_04_exceptions_logging"/"tasks.txt"

#függvények definiálása
#feladatok olvasása
def read_tasks():
    loaded_tasks = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                loaded_tasks.append(line.strip())
    except FileNotFoundError:
        logger.warning(f"A {file_path} fájl még nem létezik.")
    except Exception as e:
        logger.error(f"Váratlan hiba a fájl beolvasásakor: {e}")
    return loaded_tasks

#feladatok irása
def write_tasks(tasks):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        logger.error(f"Hiba a fájlba íráskor: {e}")

#feladatok megjelenítése
def view_tasks(tasks):
    print("\n--- Jelenlegi feladatok ---")
    if not tasks:
        print("Nincsenek feladatok a listában.")
    else:
        for task_id, task in enumerate(tasks, 1):
            print(f"{task_id} {task}")
    print("---------------------------\n")

#feladat hozzáadás
def add_task(tasks, new_task):
    tasks.append(new_task)
    logger.info(f"Új feladat hozzáadva: '{new_task}'")

#feladat törlés
def remove_task(tasks, task_str):
    try:
        task_id = int(task_str) - 1 
        if 0 <= task_id < len(tasks):
            removed = tasks.pop(task_id)
            logger.info(f"Feladat törölve: '{removed}'")
            print(f"Sikeresen törölve: {removed}")
        else:
            print("Hiba: Nincs ilyen sorszámú feladat a listában.")
    except ValueError:
        logger.error("A felhasználó nem számot adott meg törléskor.")
        print("Hiba: Kérlek, a feladat sorszámát (számot) add meg a törléshez!")

#menü
def display_menu():
    print("Menü:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

#főprogram
def main():
    tasks = read_tasks()

    while True:
        display_menu()
        choice = input("Válassz egy opciót (1-4): ").strip()

        if choice == '1':
            task = input("Írd be az új feladatot: ").strip()
            if task:
                add_task(tasks, task)
            else:
                print("A feladat nem lehet üres!")
                
        elif choice == '2':
            view_tasks(tasks)
            
        elif choice == '3':
            view_tasks(tasks)
            if tasks:
                task_str = input("Add meg a törölni kívánt feladat sorszámát: ").strip()
                remove_task(tasks, task_str)
                
        elif choice == '4':
            logger.info("Kilépés... Feladatok mentése folyamatban.")
            write_tasks(tasks)
            print("Kilépés. A feladatok mentve lettek.")
            break
            
        else:
            logger.warning(f"Érvénytelen menüválasztás: '{choice}'")
            print("Érvénytelen opció! Kérlek, 1, 2, 3 vagy 4 közül válassz.")

    logger.info("Feladatkezelő program leállt.\n")

if __name__ == "__main__":
    main()