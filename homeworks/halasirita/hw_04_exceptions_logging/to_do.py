#logolás

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("to_do.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# task lista mutatása

def read_tasks(file_path):
    try:
        with open(file_path, "r") as file:
            tasks = []

            for line in file:
                task = line.strip()

                if task:
                    tasks.append(task)

        logger.info(f"Tasks successfully loaded from {file_path}.")
        return tasks

    except FileNotFoundError as e:
        logger.error(f"Task file not found: {e}")
        return []

    except OSError as e:
        logger.error(f"Could not read task file: {e}")
        return []

# task hozzáadás

def write_tasks(tasks, file_path):
    try:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")

        logger.info(f"Tasks successfully saved to {file_path}.")

    except OSError as e:
        logger.error(f"Could not write task file: {e}")

# task mutatása

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()

    if not task:
        logger.warning("Empty task was not added.")
        print("Task cannot be empty.")
        return

    tasks.append(task)
    logger.info(f"Task added: {task}")

"""def add_task(tasks):
    task = input("Enter a new task: ").strip()
    tasks.append(task)
    logger.info(f"Task added: {task}")"""

# task törlése

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    display_tasks(tasks)

    while True:
        try:
            task_number = int(
                input("Enter the task number to remove: ")
            )

            if task_number < 1 or task_number > len(tasks):
                logger.warning("Invalid task number.")
                print("Please enter an existing task number.")
                continue

            removed_task = tasks.pop(task_number - 1)

            logger.info("Task removed successfully.")
            print(f"Task removed: {removed_task}")
            return

        except ValueError:
            logger.warning("Invalid task number input.")
            print("Please enter a number.")

# menü

def display_menu():
    print("1 - Add Task")
    print("2 - View Tasks")
    print("3 - Remove Task")
    print("4 - Exit")


def main():
    file_path = "tasks.txt"
    tasks = read_tasks(file_path)

    while True:
        display_menu()

        try:
            choice = int(input("Choose an option (1-4): "))

            if choice not in [1, 2, 3, 4]:
                logger.warning(f"Invalid menu choice: {choice}")
                continue

        except ValueError:
            logger.warning("Invalid menu input.")
            continue

        if choice == 1:
            add_task(tasks)

        elif choice == 2:
            display_tasks(tasks)

        elif choice == 3:
            remove_task(tasks)

        elif choice == 4:
            write_tasks(tasks, file_path)
            break

if __name__ == "__main__":
    main()
    