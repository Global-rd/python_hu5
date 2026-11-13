import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("to_do.log")
console_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(console_handler)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


def read_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        logger.info("Tasks loaded successfully.")
        return tasks
    except FileNotFoundError:
        logger.warning(
            "tasks.txt not found. Starting with an empty task list."
        )
        return []


def write_tasks(tasks):
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info("Tasks saved successfully.")
    except IOError:
        logger.error("An error occurred while saving tasks.")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks, task):
    tasks.append(task)
    logger.info(f"Task added: {task}")


def remove_task(tasks, task_number):
    try:
        if task_number < 1 or task_number > len(tasks):
            raise IndexError

        removed_task = tasks.pop(task_number - 1)
        logger.info(f"Task removed: {removed_task}")

    except IndexError:
        logger.error("Invalid task number.")
        print("Invalid task number.")


def display_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


tasks = read_tasks()

while True:
    display_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
        logger.warning(f"Invalid menu choice: {choice}")
        continue

    if choice == "1":
        task = input("Enter the new task: ").strip()

        if task:
            add_task(tasks, task)
            print("Task added.")
        else:
            print("Task cannot be empty.")
            logger.warning("Empty task was not added.")

    elif choice == "2":
        display_tasks(tasks)

    elif choice == "3":
        display_tasks(tasks)

        if tasks:
            try:
                task_number = int(
                    input("Enter the task number to remove: ")
                )
                remove_task(tasks, task_number)

            except ValueError:
                print("Please enter a valid number.")
                logger.error("Invalid task number input.")

    elif choice == "4":
        write_tasks(tasks)
        logger.info("Program exited.")
        print("Goodbye!")
        break
