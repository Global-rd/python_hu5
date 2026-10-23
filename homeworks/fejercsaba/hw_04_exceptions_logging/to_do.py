"""
Definiálj 5 függvényt a következőkre: feladatok olvasása, feladatok 
írása, feladatok megjelenítése, egy feladat hozzáadása, egy feladat 
törlése 
"""


import os
import logging
from pathlib import Path

user_name = os.getlogin()
task_list =[]
log_path = Path(__file__).parent / "to_do.log"
task_path = Path(__file__).parent / "to_do.txt"


logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(log_path)
        ],
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def add_task():
    task_list.append(task)
    logging.info(f"Task '{task}' recorded. user: user:{user_name}")


def view_task():
      try:
        with open(task_path, "r") as f:
            for task in f:
                task = task.strip()
                task_list.append(task)
        logging.info(f"Tasks loaded. user: user:{user_name}")
    except FileNotFoundError:
        print("The file does not exist.")
        logging.warning(f"The file to read does not exist. user user:{user_name} ")

def remove_task():
    try:    
        task_list.remove(task)
        logging.info(f"The '{task}' removed successfully. user:{user_name}")
    except ValueError:
        print("Task not found.")
        logging.warning(f"Task '{task}' does not exist. user:{user_name}")


def display_menu():
    print("1 - Add Task")
    print("2 - View Task")
    print("3 - Remove Task")
    print("4 - Exit")




display_menu()
while True:
    choice = input()
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        logging.warning(f"Invalid input.  user:{user_name}")
    if choice == "4":

        writing_task(task_list)
        logging.info(f"Application closed. user: {user_name}")
        print("Tasks saved.")
        print(f"Goodbye {use_name}!")
    elif choice == "3":
        pass

    elif choice == "2":
        pass

    elif choice == "1":
        pass

print(log_path)



