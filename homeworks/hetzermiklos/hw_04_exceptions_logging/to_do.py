
import logging
from pathlib import Path


# File paths
BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.txt"
LOG_FILE = BASE_DIR / "to_do.log"


# Logging configuration
logger = logging.getLogger("task_manager")
logger.setLevel(logging.INFO)

log_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setFormatter(log_format)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Read tasks from file
def read_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file if line.strip()]

        logger.info("Tasks loaded successfully.")
        return tasks

    except FileNotFoundError:
        logger.warning("Tasks file not found. Starting with an empty list.")
        return []

    except OSError as error:
        logger.error(f"Error reading tasks: {error}")
        return []


# Write tasks to file
def write_tasks(tasks):
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")

        logger.info("Tasks saved successfully.")
        return True

    except OSError as error:
        logger.error(f"Error saving tasks: {error}")
        return False


# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour tasks:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


# Add a new task
def add_task(tasks, task):
    task = task.strip()

    if not task:
        print("Task cannot be empty.")
        logger.warning("Attempted to add an empty task.")
        return

    if "\n" in task or "\r" in task:
        print("Task cannot contain line breaks.")
        logger.warning("Attempted to add a task with line breaks.")
        return

    tasks.append(task)
    print("Task added successfully.")
    logger.info(f"Task added: {task}")


# Remove an existing task
def remove_task(tasks, task_number):
    try:
        index = int(task_number) - 1

        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            logger.warning("Invalid task number entered.")
            return

        removed_task = tasks.pop(index)

        print("Task removed successfully.")
        logger.info(f"Task removed: {removed_task}")

    except ValueError:
        print("Please enter a valid number.")
        logger.warning("Non-numeric task number entered.")


# Display the menu
def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


# Main program
def main():
    tasks = read_tasks()

    logger.info("Task Manager started.")

    while True:
        display_menu()

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter a new task: ")
            add_task(tasks, task)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)

            if tasks:
                task_number = input("Enter task number to remove: ")
                remove_task(tasks, task_number)

        elif choice == "4":
            if write_tasks(tasks):
                logger.info("Task Manager closed.")
                print("Goodbye!")
                break

            print("Could not save tasks. Please try again.")

        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")
            logger.warning(f"Invalid menu option: {choice}")


if __name__ == "__main__":
    main()
