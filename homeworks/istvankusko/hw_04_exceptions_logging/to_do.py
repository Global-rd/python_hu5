#to do task
import logging
import sys

# ---------  Questions for István
# How do you check for the presence of modules to be loaded?
# Where should I put timesamp?  In every logging statement?    How does it work in a real-world application?

# Logging configuration: writes to both the console and a .log file at the same time
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("to_do.log", encoding="utf-8"),  # az encoding így jó? vagy máshogy kell használni?
        #logging.StreamHandler(sys.stdout)
    ]
)

TASKS_FILE = "tasks.txt"

def read_tasks(filename):
    """Load tasks from the file when the program starts."""
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        logging.info(f"Tasks successfully loaded from here: {filename}")
    except FileNotFoundError:
        logging.warning(f"The file cannot be found ({filename}). Let's start with a new, empty list.")
    except Exception as e:
        logging.error(f"An error occurred while reading the file: {e}")
    return tasks

def write_tasks(filename, tasks):
    """Write the tasks to the file when the program closes (overwrite)."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        logging.info(f"Tasks successfully saved here: {filename}")
    except Exception as e:
        logging.error(f"An error occurred while writing the file: {e}")

def display_tasks(tasks):
    """Displaying tasks on the console."""
    if not tasks:
        print("\nThere are no tasks on the list.")
        logging.info("List of tasks: The list is empty.")
    else:
        print("\n--- Current Tasks ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        logging.info("The tasks have been successfully listed.")

def add_task(tasks, task_name):
    """Add a new task to the list stored in memory."""
    if task_name.strip():
        tasks.append(task_name.strip())
        print(f"'{task_name.strip()}' Successfully added.")
        logging.info(f"Task added: {task_name.strip()}")
    else:
        print("The assignment name cannot be left blank!")
        logging.warning("An attempt was made to add an empty task.")

def remove_task(tasks, task_index_str):
    """Delete a task based on the specified serial number."""
    try:
        index = int(task_index_str) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"'{removed}' Successfully deleted.")
            logging.info(f"Task deleted: {removed}")
        else:
            print("Invalid problem number! There is no such problem.")
            logging.warning(f"Deletion attempt with an invalid serial number: {task_index_str}")
    except ValueError:
        print("Please enter a valid number!")
        logging.warning(f"To delete invalid input (non-numeric): {task_index_str}")

def display_menu():
    """Menu"""
    print("\n--- Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    logging.info("The Task Manager application has started.")
    tasks = read_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("\nSelect an option (1–4): ").strip()

        if choice == "1":
            task_name = input("Enter the name of the new task: ")
            add_task(tasks, task_name)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                task_idx = input("Enter the number of the task you want to delete: ")
                remove_task(tasks, task_idx)
        elif choice == "4":
            write_tasks(TASKS_FILE, tasks)
            print("\nLog out... Goodbye!")
            logging.info("The Task Manager application has closed.")
            break
        else:
            print("Invalid selection! Please enter a value of 1, 2, 3, or 4.")
            logging.warning(f"Invalid menu selection: {choice}")

if __name__ == "__main__":
    main()