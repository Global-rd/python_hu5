import logging

TASKS_FILE = "tasks.txt"
LOG_FILE = "to_do.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)


def read_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
            logging.info("Tasks loaded successfully.")
            return tasks

    except FileNotFoundError:
        logging.warning(
            "Tasks file not found. Starting with an empty task list."
        )
        return []

    except Exception as error:
        logging.error(f"Error while reading tasks: {error}")
        return []


def write_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")

        logging.info("Tasks saved successfully.")

    except Exception as error:
        logging.error(f"Error while saving tasks: {error}")


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nCurrent Tasks:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print()


def add_task(tasks, task):
    tasks.append(task)
    logging.info(f"Task added: {task}")


def remove_task(tasks, task_number):
    # Guard clause
    if task_number < 1:
        print("Task number cannot be lower than 1.")
        logging.warning(
            "User entered a task number lower than 1."
        )
        return

    try:
        removed_task = tasks.pop(task_number - 1)
        logging.info(f"Task removed: {removed_task}")

    except IndexError:
        print("Invalid task number.")
        logging.warning(
            "User tried to remove a non-existing task."
        )


def display_menu():
    print("\n===== TO-DO APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    tasks = read_tasks()

    while True:
        display_menu()

        choice = input(
            "Select an option (1-4): "
        ).strip()

        if choice not in ["1", "2", "3", "4"]:
            print(
                "Invalid option. Please choose between 1 and 4."
            )
            continue

        if choice == "1":
            task = input(
                "Enter task description: "
            ).strip()

            if task:
                add_task(tasks, task)
            else:
                print(
                    "Task description cannot be empty."
                )

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)

            try:
                task_number = int(
                    input(
                        "Enter the task number to remove: "
                    )
                )

                remove_task(tasks, task_number)

            except ValueError:
                print("Please enter a valid number.")
                logging.warning(
                    "Invalid task number entered."
                )

        elif choice == "4":
            write_tasks(tasks)
            logging.info("Application closed.")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()