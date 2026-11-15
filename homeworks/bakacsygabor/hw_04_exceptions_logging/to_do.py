import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.txt"
LOG_FILE = BASE_DIR / "to_do.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def read_tasks():
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = []

            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)

        logging.info("%d feladat betöltve.", len(tasks))
        return tasks

    except FileNotFoundError:
        logging.warning("A tasks.txt nem található; üres listával indulunk.")
        return []

    except OSError:
        logging.exception("Nem sikerült beolvasni a feladatokat.")
        raise


def write_tasks(tasks):
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task}\n")

        logging.info("%d feladat elmentve.", len(tasks))
        return True

    except OSError:
        logging.exception("Nem sikerült elmenteni a feladatokat.")
        return False


def display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\nTasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task(tasks, task):
    task = task.strip()

    if not task:
        print("Task cannot be empty.")
        logging.warning("Üres feladatot próbáltak hozzáadni.")
        return

    tasks.append(task)
    logging.info("Feladat hozzáadva: %s", task)
    print("Task added.")


def remove_task(tasks, task_number):
    if not tasks:
        print("No tasks to remove.")
        return

    try:
        index = int(task_number) - 1
    except ValueError:
        print("Please enter a valid number.")
        logging.warning("Nem számot adtak meg törléshez: %s", task_number)
        return

    if index < 0 or index >= len(tasks):
        print("There is no task with that number.")
        logging.warning("Nem létező feladatsorszám: %s", task_number)
        return

    removed_task = tasks.pop(index)
    logging.info("Feladat törölve: %s", removed_task)
    print(f"Removed task: {removed_task}")


def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
def main():
    try:
        tasks = read_tasks()
    except OSError:
        print("Could not load tasks. The program will stop to protect your data.")
        return

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice not in ("1", "2", "3", "4"):
            print("Please choose 1, 2, 3, or 4.")
            logging.warning("Érvénytelen menüpont: %s", choice)
            continue

        if choice == "1":
            new_task = input("Enter a new task: ")
            add_task(tasks, new_task)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                task_number = input("Enter the task number to remove: ").strip()
                remove_task(tasks, task_number)
        elif choice == "4":
            if write_tasks(tasks):
                print("Tasks saved. Goodbye!")
                logging.info("Program bezárva.")
                break
            print("Saving failed. Please try again.")


if __name__ == "__main__":
    main()