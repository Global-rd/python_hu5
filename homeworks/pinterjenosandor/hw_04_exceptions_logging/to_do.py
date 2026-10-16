"""import the modules"""
import logging
import os
from pathlib import Path
#basic logging, put all files to the directory where the code is run
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("to_do_logger.log"),
        #logging.StreamHandler(),
    ],
)
FILENAME = "tasks.txt"

#read the tasks from the file with logging
def read_tasks(filename):
    tasks = []
    try:
        if os.path.exists(filename): #file check
            with open(filename, "r") as file:
                for line in file:
                    task = line.strip()
                    if task:
                        tasks.append(task)
            logging.info(f"Loaded {len(tasks)} tasks from the {filename}") #show the numbers of the tasks
        else:
            logging.info(f"{filename} doesn't exist, the program make it!") #check if the file available
    except Exception as error:
            logging.error(f"error at file reading {error}") #file reading error 
    return tasks

def write_tasks(filename, tasks):
    try:
        with open(filename, "w") as file:
                for task in tasks:
                    file.write(task + "\n")
        logging.info(f"Saved {len(tasks)} tasks to the {filename}") #show the numbers of the tasks
    except Exception as error:
        logging.error(f"error at file write {error}") #file write error 
    return tasks

"""
Add task + loggings
"""
def add_task(tasks):
    print("\n Please add a task")
    new_task = input("Please add the new task: ").strip()
    if new_task:
        tasks.append(new_task)
        write_tasks(FILENAME, tasks)
        print(f"Task {new_task} added to the list")
        logging.info(f"Task added: {new_task}")
    else:
        print(f"The line must not be empty!")
        logging.warning("Try to make empty line!")

def show_tasks(tasks):
    print("There is your issue list:")
    if not tasks:
        print("the list is empty!")
        logging.info("the user is open the list view, but it was empty!")
    else:
        for id_num, t in enumerate(tasks, start=1):
            print(f"{id_num}.\t{t}")
        logging.info(f"Displayed items: {len(tasks)}")

def remove_tasks(tasks):
    print("Which task would you like to delete")
    if not tasks:
        print("The task list is empy!")
        logging.info("The user was try to delete item from the empy list")
    else:
        for id_num, t in enumerate(tasks, start=1):
            print(f"{id_num}.\t{t}")
        try:
            delete_number = int(input("Add the number of the item what you want to delete: "))
            if 1 <= delete_number <= len(tasks):
                deleted = tasks.pop(delete_number -1)
                write_tasks(FILENAME, tasks)
                print("The item deleted!")
                logging.info(f"item deleted by the user: {deleted}, ID:{delete_number}")
            else:
                print("Invalid task number!")
                logging.warning("the user try to delete invalid task ID 'non-existent'")
        except ValueError:
            print("Invalid value, please add a number!")
            logging.warning("invalid value, the entered value not integer")

"""
Show the menu and check the option is valid or not
"""
def choose_menu():
    choose_items = ["Add task" , "View Task" , "Remove task" , "Exit"]
    print("\n Hello I'm your To do list")
    for i, choice in enumerate(choose_items, 1):
        print(f"{i}.\t{choice}")
    while True:
        try:
            choice = int(input("Please select from the menu(1-4): ").strip())
            if 1 <= choice <=4:
                return choice
            else:
                print("Invalid number, try again!")
                logging.warning("user enter invalid menu option {choice}")
        except ValueError:
            print("plz. add a number")
            logging.warning("user entered a non integer value")

def main():

    logging.info("App start")
    tasks = read_tasks(FILENAME)

    while True:
        user_choice = choose_menu()
        if user_choice == 1:
            add_task(tasks)
        elif user_choice == 2:
            show_tasks(tasks)
        elif user_choice == 3:
            remove_tasks(tasks)
        else:
            print("See you!")
            logging.info("user exit")
            break 

if __name__ == "__main__":
    main()