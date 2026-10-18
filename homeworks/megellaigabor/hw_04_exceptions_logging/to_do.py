# blatantly stealing from the lessons.
from logging_setup import setup_logging
import logging
import os
from pathlib import Path

setup_logging()
logger = logging.getLogger(__name__) #__main__

#CONSTANTS: one for the file path and one for the menu options
TASKS_FILE = Path(__file__).parent / "tasks.txt"

MENU = {
    1: "Add task",
    2: "View tasks",
    3: "Remove task",
    0: "Exit",
}

# Reading the tasks and checking for the right format (no commas allowed in the task)
def read_tasks(file_path):# read tasks from a file or database
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    tasks = [line.strip() for line in lines]

    for task in tasks:
        if "," in task:
            raise ValueError(f"Invalid task format, found commas in: {task}")
        
    return tasks

# Writing the tasks to the file
def write_tasks(file_path, tasks): # write tasks to a file or database at the end of the program
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Enamurating and printing the tasks. Also, checking if the list is empty.
def show_tasks(tasks): 
    if not tasks:
        print("No tasks left. Enjoy your day!")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

# Updating the tasks in the memory only by adding a new element
def add_task(task, tasks): 
    tasks.append(task)

# Same here, bt removing
def remove_task(number, tasks): 
    return tasks.pop(number - 1) 

# CHeckin for integer as a user input, and logging the invalid input
def user_input_number(prompt): # expects an integer
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            logger.warning(f"Invalid input for number: {user_input}")

# Checking for a string and sorting empty input and commas out
def user_input_string(prompt): 
    while True:
        user_input = input(prompt).strip()

        if not user_input.strip():
            print("Input cannot be empty. Please enter a valid string.")
            logger.warning("Empty input received for string.")
            return user_input_string(prompt)  
        elif "," in user_input:
            print("Input cannot contain commas. Please enter a valid string.")
            logger.warning(f"Invalid input for string (contains comma): {user_input}")
            return user_input_string(prompt)
        else:
            return user_input  

# Diyplaing the menu
def display_menu():
    print("\n--- Task Manager ---")
    for number, menu_option in MENU.items():
        print(f"{number}. {menu_option}")

# Navigating in the menu
def handle_menu_choice(choice, tasks):
    while True:
        display_menu()
        choice = user_input_number("Enter your choice: ")
        if choice in MENU:
            return choice
        print("Invalid choice. Please select a valid menu option.")
        logger.warning(f"Invalid menu choice: {choice}")

# Main function to run the program
def main():
    # read the tasks from the file and check for missing file or invalid format
    try:
        tasks = read_tasks(TASKS_FILE) 
    except FileNotFoundError as error:
        logger.error(f"Tasks file not found: {error}")
        return

    # rotating the menu
    while True:
        choice = handle_menu_choice(None, tasks)
        # adding a task
        if choice == 1:
            task = user_input_string("Enter the task to add: ")
            add_task(task, tasks)
            logger.info(f"Task added: {task}")
        # viewing the tasks
        elif choice == 2:
            show_tasks(tasks)
        # removing a task
        elif choice == 3:
            show_tasks(tasks)
            if tasks:
                number = user_input_number("Enter the task number to remove or press 0 to cancel: ")
                if number == 0:
                    print("Did not remove any task.")
                    continue
                elif 1 <= number <= len(tasks):
                    removed_task = remove_task(number, tasks)
                    logger.info(f"Task removed: {removed_task}")
                else:
                    print("Invalid task number.")
                    logger.warning(f"Invalid task number for removal: {number}")
        # exit and save
        elif choice == 0:
            write_tasks(TASKS_FILE, tasks)
            print("Exiting the program. Goodbye!")
            break

main()    