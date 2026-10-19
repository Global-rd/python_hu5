
# Homework 04 - Task Manager
# Simon David

import logging
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.txt"
LOG_FILE = BASE_DIR / "app.log"

# Configure logging to console and file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Store tasks in memory
tasks = []


# Read tasks from file
def read_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            loaded_tasks = [
                line.strip() for line in file if line.strip()
            ]

        logging.info("Tasks loaded successfully.")
        return loaded_tasks

    except FileNotFoundError:
        logging.warning("Task file not found. Starting with an empty list.")
        return []

    except OSError as error:
        logging.error(f"Error reading tasks: {error}")
        return []


# Write tasks to file
def write_tasks():
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task}\n")

        logging.info("Tasks saved successfully.")

    except OSError as error:
        logging.error(f"Error saving tasks: {error}")


# Display available menu options
def display_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


# Display all tasks
def view_tasks():
    if not tasks:
        print("Your task list is empty.")
        return

    print("\n===== YOUR TASKS =====")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


# Add a new task
def add_task(task):
    task = task.strip()

    if not task:
        print("Task cannot be empty.")
        logging.warning("Attempted to add an empty task.")
        return

    tasks.append(task)
    print("Task added successfully!")
    logging.info(f"Task added: {task}")


# Remove a task by its number
def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task removed: {removed_task}")
        logging.info(f"Task removed: {removed_task}")
    else:
        print("Invalid task number.")
        logging.warning(f"Invalid task number: {task_number}")


# Load saved tasks when the program starts
tasks = read_tasks()

logging.info("Task Manager started.")

# Main application loop
while True:
    display_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        new_task = input("Enter a new task: ")
        add_task(new_task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()

        if tasks:
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)

            except ValueError:
                print("Please enter a valid number.")
                logging.warning("Invalid task number input.")

    elif choice == "4":
        write_tasks()
        logging.info("Task Manager closed.")
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-4.")
        logging.warning(f"Invalid menu option: {choice}")
