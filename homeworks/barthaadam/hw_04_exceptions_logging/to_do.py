import logging
from pathlib import Path


# Store the files in the same folder as this Python script.
BASE_DIR = Path(__file__).resolve().parent
TASK_FILE = BASE_DIR / "to_do.txt"


#Read tasks from the file when the program starts.
def read_tasks():
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file if line.strip()]

        logging.info("Number of tasks loaded: %s", len(tasks))
        return tasks

    except FileNotFoundError:
        logging.warning("tasks.txt was not found. Starting with an empty list.")
        return []

    except (OSError, UnicodeError):
        logging.exception("Failed to read tasks.")
        raise


#Overwrite the file with the current tasks when exiting.
def write_tasks(tasks):
    try:
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")

        logging.info("Tasks saved successfully.")
        return True

    except (OSError, UnicodeError):
        logging.exception("Failed to save tasks.")
        return False


#Display tasks with numbers starting from 1.
def view_tasks(tasks):
    if not tasks:
        print("There are no tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


#Add a non-empty task to the list.
def add_task(tasks, task):
    task = task.strip()

    if not task:
        print("The task cannot be empty!")
        logging.warning("Attempted to add an empty task.")
        return

    tasks.append(task)
    logging.info("Task added: %s", task)


#Remove a task using its displayed number.
def remove_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        logging.info("Task removed: %s", removed_task)
    else:
        print("There is no task with that number!")
        logging.warning("Invalid task number: %s", task_number)


#Display the available menu options.
def display_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


#Send log messages to both the console and a log file.
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                BASE_DIR / "task_manager.log",
                encoding="utf-8",
            ),
        ],
    )


#Load tasks once, when the program starts.
    try:
        tasks = read_tasks()

#Avoid overwriting existing tasks after a reading error.
    except (OSError, UnicodeError):
        print("The program cannot start because the task file could not be read.")

    else:
        while True:
            display_menu()
            choice = input("Choose an option (1–4): ").strip()

            if choice not in ("1", "2", "3", "4"):
                print("Please enter 1, 2, 3, or 4!")
                logging.warning("Invalid menu option: %s", choice)
                continue

            if choice == "1":
                task = input("Enter a new task: ")
                add_task(tasks, task)

            elif choice == "2":
                view_tasks(tasks)

            elif choice == "3":
                view_tasks(tasks)

                if not tasks:
                    continue

                try:
                    task_number = int(
                        input("Enter the number of the task to remove: ")
                    )

                except ValueError:
                    print("Please enter a whole number!")
                    logging.warning("The task number was not an integer.")

                else:
                    remove_task(tasks, task_number)

#Save tasks only when the user selects Exit.
            elif choice == "4":
                if write_tasks(tasks):
                    print("Goodbye!")
                    break

                print("Saving failed. Your tasks are still in memory.")
