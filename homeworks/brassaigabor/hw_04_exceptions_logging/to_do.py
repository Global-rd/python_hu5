
import os
import logging

#-----------------------------------

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Fájl: INFO szint, teljes traceback
file_handler = logging.FileHandler("./hw_04_exceptions_logging/todo.log", mode="a",)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Konzol: ERROR szint, traceback nélkül
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

logger.addHandler(file_handler)
logger.addHandler(console_handler)

#-----------------------------------

def add_task():
#    print("add")
    todo_list.append(input("Type new todo list item: "))   #beszurja  alista vegere az uj todo elemet

#-----------------------------------

def view_task():
#    print("view")
#    print(*todo_list, sep="\n") # uj sorokba kilistazza a lista elemeit
    for i, task in enumerate(todo_list):
        print(f"{i} - {task}")

#-----------------------------------

def remove_task():
#    print("remove")
    view_task()
    while 1:
        try:
            instruction = int(input("Choose a todo item number: "))
            todo_list.pop(instruction)
            break
        except ValueError:
            print("Invalid task number")
            logger.warning("Remove task - invalid task number")
            continue
        except IndexError:
            print("Invalid task number")
            logger.warning("Remove task - invalid task number")
            continue
    
#-----------------------------------

def exit_task():
    with open("./hw_04_exceptions_logging/todo_list.txt", "w") as f:
        f.writelines(line + "\n" for line in todo_list)
#    print("exit")

#-----------------------------------

def display_menu():
    while True:
        os.system("cls")
        print("""
        1 - Add task
        2 - View task
        3 - Remove task
        4 - Exit
        """)

        try:
            instruction = int(input("Choose a menu, please: "))
        except ValueError:
#            input("Please enter a number! Press Enter...")
            logger.warning("Menu selector (display_menu) - Invalid menu number")
            continue

        if instruction not in submenu:
#            input("Invalid menu! Press Enter...")
            logger.warning("Menu selector (display_menu) - Invalid menu number")
            continue

        submenu[instruction]()

        if instruction == 4:
            break

        input("Press Enter to continue...")

#-----------------------------------

submenu = {
    1: add_task,
    2: view_task,
    3: remove_task,
    4: exit_task
}

try:
    with open("./hw_04_exceptions_logging/todo_list.txt", "r") as f:
        todo_list = [line.strip() for line in f]
except FileNotFoundError:
    logger.exception("File opening error (File not found) - todo_list.txt")
    todo_list = []    

display_menu()
