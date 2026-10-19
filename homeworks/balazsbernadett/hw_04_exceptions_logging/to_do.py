import os
from pathlib import Path
import logging
import logging.config
from logging_setup import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

file_path = Path("homeworks") /"balazsbernadett"/ "hw_04_exceptions_logging"/ "hw04.txt"
tasks = []

def task_read():
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                tasks.append(line.strip())
    except FileNotFoundError as e:
        logger.exception(f"An error occurred: {e}")

def task_write():
    try:
        print(file_path.resolve())
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n") 
    except Exception as e:
        logger.exception(f"An error occurred: {e}")

def task_display():
        if not tasks:
            print("Don't have task")
        else:
            for i, task in enumerate(tasks, 1):
                print(i,task)
        return tasks

def task_add(task):
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append(task)
    
def task_delete(d_task):
    
    if 1 <= d_task <= len(tasks):
        del tasks[d_task-1]
    else:
        print("There is no task with this number.")

def display_menu():
    logger.info("Application started.")
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("What do you want to do? 1,2,3,4?")

        if choice == "1":
            task = input("Enter a task: ")
            task_add(task)
        elif choice == "2":
            task_display()
        elif choice == "3":
            task_display()
            d_task= int(input("Which sequence number are you deleting?"))
            task_delete(d_task)
        elif choice == "4":
             task_write()
             logger.info("Application closed.")
             break
        else: 
            print("Wrong choice. You can only choose 1, 2, 3, or 4.")

task_read()
display_menu()