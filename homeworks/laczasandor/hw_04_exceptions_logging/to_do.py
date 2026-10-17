"""
Task manager application (homework 4).
 
The tasks are loaded from a text file when the program starts, kept in
memory (in a list) while the program runs, and written back to the file
only when the user chooses "Exit".
Every important event is logged to the console and to a .log file at the
same time.
"""
 
import logging
from pathlib import Path
 
# The files are stored next to this script, so the program works the same
# way no matter which folder it is started from (e.g. from VS Code).
BASE_DIR = Path(__file__).parent
TASKS_FILE = BASE_DIR / "tasks.txt"
LOG_FILE = BASE_DIR / "to_do.log"
 
MENU_OPTIONS = ("1", "2", "3", "4")
 
 
def setup_logger():
    """
    Create a logger that writes to the console and to a log file.
 
    Returns:
        logging.Logger: The configured logger.
    """
    logger = logging.getLogger("to_do")
    logger.setLevel(logging.DEBUG)
 
    # Do not add the handlers twice if the function is called again
    if logger.handlers:
        return logger
 
    # StreamHandler: console output (shorter format, INFO and above)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
 
    # FileHandler: log file (full format with timestamp, DEBUG and above)
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
 
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
 
 
logger = setup_logger()
 
 
def read_tasks(file_path):
    """
    Read the tasks from a text file (one task per line).
 
    Parameters:
        file_path (Path): Path of the tasks file.
 
    Returns:
        list: The tasks read from the file. Empty list if the file
        does not exist or cannot be read.
    """
    tasks = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        logger.warning(f"'{file_path.name}' not found, starting with an empty task list.")
    except OSError as error:
        logger.error(f"Could not read '{file_path.name}': {error}")
    else:
        logger.info(f"{len(tasks)} task(s) loaded from '{file_path.name}'.")
    return tasks
 
 
def write_tasks(file_path, tasks):
    """
    Write the tasks to a text file, overwriting its previous content.
 
    Parameters:
        file_path (Path): Path of the tasks file.
        tasks (list): The tasks to save.
 
    Returns:
        bool: True if the save was successful, False otherwise.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
    except OSError as error:
        logger.error(f"Could not write '{file_path.name}': {error}")
        return False
    else:
        logger.info(f"{len(tasks)} task(s) saved to '{file_path.name}'.")
        return True
 
 
def display_tasks(tasks):
    """
    Print the tasks with their order numbers.
 
    Parameters:
        tasks (list): The tasks to display.
    """
    if not tasks:
        print("\nThe task list is empty.")
        return
 
    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"  {number}. {task}")
    logger.debug(f"{len(tasks)} task(s) displayed.")
 
 
def add_task(tasks, task):
    """
    Add a new task to the end of the task list.
 
    Parameters:
        tasks (list): The task list (modified in place).
        task (str): The text of the new task.
    """
    task = task.strip()
    if not task:
        logger.warning("Empty task was not added.")
        return
 
    tasks.append(task)
    logger.info(f"Task added: '{task}'")
 
 
def remove_task(tasks, task_number):
    """
    Remove a task by its order number (as shown by display_tasks).
 
    Parameters:
        tasks (list): The task list (modified in place).
        task_number (int): The order number of the task, starting from 1.
    """
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        logger.info(f"Task removed: '{removed_task}'")
    else:
        logger.warning(f"Invalid task number: {task_number} (valid: 1-{len(tasks)})")
 
 
def display_menu():
    """Print the available menu options."""
    print("\n===== TO-DO MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
 
 
def main():
    """Run the task manager until the user chooses Exit."""
    logger.debug("Application started.")
    tasks = read_tasks(TASKS_FILE)
 
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
 
        if choice not in MENU_OPTIONS:
            logger.warning(f"Invalid menu option: '{choice}'. Please enter 1, 2, 3 or 4.")
            continue
 
        if choice == "1":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
 
        elif choice == "2":
            display_tasks(tasks)
 
        elif choice == "3":
            display_tasks(tasks)
            if not tasks:
                continue
            try:
                task_number = int(input("Enter the number of the task to remove: "))
            except ValueError:
                logger.warning("The task number must be a whole number.")
            else:
                remove_task(tasks, task_number)
 
        elif choice == "4":
            write_tasks(TASKS_FILE, tasks)
            logger.info("Application closed. Goodbye!")
            break
 
 
if __name__ == "__main__":
    main()
 