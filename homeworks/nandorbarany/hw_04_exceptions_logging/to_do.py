import logging
import logging.config
from pathlib import Path

# logging setup

LOG_DIR = Path("hw_04_exceptions_logging")
LOG_DIR.mkdir(exist_ok=True)

FILE_PATH = Path("todo_tasks.txt")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "to_do.log",
            "maxBytes": 10_000_000,
            "backupCount": 5,
            "formatter": "default",
            "level": "DEBUG",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}

# functions
def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)


setup_logging()
logger = logging.getLogger(__name__ == "to_do")


def read_file_line_by_line(file_path):
    """
    soronkénti beolv
    """
    with open(file_path, "r") as file:
        for line in file:
            yield line

def read_tasks(file_path):
    """
    feladatok beolvasása, listaként tárolás
    """
    tasks = []
    try:
        for line in read_file_line_by_line(file_path=file_path):
            line = line.strip()
            if line:
                tasks.append(line)
        logger.info(f"{len(tasks)} tasks loaded from file.")
    except FileNotFoundError as e:
        logger.warning(f"File not found, starting with an empty list. {e}")
    except Exception as e:
        logger.exception(f"Error while reading file: {e}")
    return tasks

def write_tasks(tasks, file_path):
    """
    feladatok írása
    """
    try:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info("Tasks saved to file.")
    except Exception as e:
        logger.exception(f"Error while writing file: {e}")


def view_tasks(tasks):
    """
    feladatok megjelenítése
    """
    logger.info("Displaying tasks.")
    if len(tasks) == 0:
        print("No tasks in file.")
        return
    for number, task in enumerate(tasks, 1):
        print(f"{number} - {task}")


def add_task(tasks, task):
    """
    feladat hozzáadása a listához
    """
    tasks.append(task)
    logger.info(f"Task added: {task}")


def remove_task(tasks, number):
    """
    feladat törlése a listából
    """
    if number < 1 or number > len(tasks):
        logger.warning(f"Invalid task number: {number}")
        return
    task = tasks[number - 1]
    tasks.remove(task)
    logger.info(f"Task removed: {task}")


def display_menu():
    """
    Prints the menu options.
    """
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    logger.info("Application started.")
    tasks = read_tasks(file_path=FILE_PATH)

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice < "1" or choice > "4":
            logger.warning(f"Invalid menu choice: {choice}")
            print("Please enter 1, 2, 3 or 4.")
        elif choice == "1":
            task = input("Enter the task: ")
            add_task(tasks=tasks, task=task)
        elif choice == "2":
            view_tasks(tasks=tasks)
        elif choice == "3":
            view_tasks(tasks=tasks)
            try:
                number = int(input("Enter the number of the task to remove: "))
                remove_task(tasks=tasks, number=number)
            except ValueError as e:
                logger.warning(f"The task number must be an integer. {e}")
        elif choice == "4":
            write_tasks(tasks=tasks, file_path=FILE_PATH)
            logger.info("Application finished.")
            break

main()