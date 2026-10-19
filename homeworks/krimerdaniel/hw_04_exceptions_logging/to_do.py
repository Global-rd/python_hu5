"""
TASK MANAGER - A 'TO DO' LIST
It lets the user add, remove, and view tasks of their 'To do' list and saves it into a to_do_list.txt file.
"""

##Import and initial setup

import os
os.system("cls")
from pathlib import Path
import re
from logging_setup import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

file_path = Path("homeworks") /"krimerdaniel"/ "hw_04_exceptions_logging" / "to_do_list.txt"


##The main function
"""
Runinng the programme offering 4 options:
1. Add task(s)
2. View tasks
3. Remove task(s)
4. Exit the program
"""

def main():
    logger.info("Application started.")
    open_file()    
    while True:
        display_menu()
        try:
            if option == 1:
                add_task()
            elif option == 2:
                view_list()
            elif option == 3:
                remove_task()
            elif option == 4:
                exit_prog()
        except Exception as e:
            logger .exception(f"Hmm, it should'n have happened, something went sideways...quiting Task Manager. {e}")
        

## Functions in use
"""
Opening existing or creating to do list file and reading in its content line by line
"""

def open_file():
    global to_do_list
    to_do_list = []
    try:
        with open(file_path, 'a+') as file:
            file.seek(0)
            to_do_list = file.read().splitlines()
        print("Welcome to your 'To do' list! Manage it as you see fit.")
        logger.info("File opened / created, its content is read in to list.")
    except FileNotFoundError as e:
        logger.error(f"File not found. {e}")


# Displaying menu options
"""
Displaying main menu:
- asks for user input from available options
- handles errors
- repeats as long as correct input provided
"""

def display_menu():
    while True:
            try:
                global option
                option = int(input("Please select an option by entering its ordinal number (i.e. 1)\n"
                  "\t1. Add a new task\n"
                  "\t2. View 'To do' list\n"
                  "\t3. Remove a task\n"
                  "\t4. Exit\n"))
                if option in [1, 2, 3, 4]:
                    logger.info("Display menu - correct selection is made.")
                    return
                else:
                    print(f"Your selection ({option}) is not in the available options (1, 2, 3, or 4), try again.")
                    logger.info("Display menu - integer provided, but out of range.")
            except ValueError as e:
                print("You should provide 1, 2, 3, or 4, try again.")
                logger.exception(f"Display menu - not an integer is provided. {e}")


# Adding a task to list
"""
Add a task:
- asks user to enter a single task - as a single task can be described by more than one words
(i.e. "clean the dishes", or "take the dog for a walk", thus each user input is considered as one task
- adds the one task to the end of the 'to do' list
- returns to main menu
"""

def add_task():
    new_task = input("Please enter a new task to add to your 'To do' list: ")
    try:
        if new_task in to_do_list:
            print(f"'{new_task}' is already on your 'To do' list, makes no sense to add it once more.\n")
            logger.info("Add task - task is already in list.")
        elif new_task == 'cancel':
            print("You have cancelled adding a new task to your 'To do' list.\n")
            logger.info("Add task - 'cancel'.")
            return
        else:
            to_do_list.append(new_task.strip())
            print(f"New task ({new_task}) has been added to your 'To do' list.\n")
            logger.info("Add task - new task added.")
    except NameError as e:
        logger.exception(f"Something unexpected occured. {e}")


# Viewing to do list
"""
View tasks:
- checks if 'To do' list has any items
- if so, prints out all the task(s) in a new line from the 'to do' list
- returns to main menu
"""

def view_list():
    if len(to_do_list) == 0:
        print("Your 'To do' list is currently empty. Add a task by option 1.\n")
        logger.info("View list - list is empty.")
    else:
        print(f"Your current 'To do' list consists of {len(to_do_list)} task(s):")
        for item in to_do_list: print(f"\t{to_do_list.index(item)+1} {item}")
        logger.info("View list - list is printed.")


# Removing a task from to do list either by order or name
"""
Remove a task:
- prints out all the task item(s) in a new line - as a hint so the user knows what tasks are on the 'to do' list
- asks for a task to remove
- handles error
- removes the one task from the 'to do' list
- returns to main menu
"""

def remove_task():
    if len(to_do_list) == 0:
        print("Your 'To do' list is currently empty, there is nothing to remove. Add a task by option 1.\n")
        logger.info("Remove task - list is empty.")
    else:
        print(f"Your current 'To do' list consists of {len(to_do_list)} task(s):")
        for item in to_do_list: print(f"\t{to_do_list.index(item)+1} {item}")
        task_to_remove = input("Please enter a task either by its ordinal number or by its name to remove from your 'To do' list: ")
        match = re.fullmatch(r"(\d+)(?:\.|(?:st|nd|rd|th))?", task_to_remove)
        if match:
            try:
                task_index = int(match.group(1)) - 1
                print(f"Task {task_index + 1} ({to_do_list[task_index]}) has been removed from your 'To do' list.")
                to_do_list.pop(task_index)
                logger.info("Remove task - task removed by index.")
                return
            except IndexError as e:
                print(f"The list has only {len(to_do_list)} item, the provided ordinal number {task_index + 1} is out of range.")
                logger.info(f"Remove task - index is out of range. {e}")
        else:
            task_to_remove = task_to_remove.strip().lower()
            try:
                if task_to_remove in to_do_list:
                    to_do_list.remove(task_to_remove)
                    print(f"'{task_to_remove}' has been removed from your 'To do' list.\n")
                    logger.info("Remove task - task removed by name.")
                elif task_to_remove == 'cancel':
                    print("You have cancelled removing a task from your 'To do' list.\n")
                    logger.info("Remove task - cancel.")
                    return
                else:
                    print(f"'{task_to_remove}' is not in your 'To do' list, thus it cannot be removed.\n")
                    logger.info("Remove task - task is not in list by name.")
            except Exception as e:
                logger.exception(f"Something unexpected occured. {e}")
           
# writng the tasklist into file and and informing user, exiting the program 
"""
Exit the program:
- saves changes of the 'to do' list and overwrites the file
- exits the program
"""

def exit_prog():
    try:
        with open(file_path, 'w') as file:
            for task in to_do_list:
                file.write(task + "\n")
            logger.info("Exit prog - list is written into file.")
        if len(to_do_list) == 0:
            print("Quiting Task Manager. Your current 'To do' list has no tasks, it is saved empty.")
        else:
            print(f"Quiting Task Manager. Your current 'To do' list is saved with {len(to_do_list)} task(s):")
            for item in to_do_list: print(f"\t{to_do_list.index(item)+1} {item}")
    except Exception as e:
        logger.exception(f"Something unexpected happened: {e}")

    exit()




main()