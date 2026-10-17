import logging
from pathlib import Path

# Setting up logging configuration

log_file_path = Path(__file__).parent / 'app.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

# Creating the functions for the to-do list

file_path = Path(__file__).parent / 'to_do_list.txt'
task_list = []

def display_menu():
    print("\nPlease select an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def read_tasks():
    try:
        with open(file_path, 'r') as file:
            task_list[:] = [line.rstrip('\n') for line in file]
    except FileNotFoundError:
            logging.error("The to-do list file was not found.")
            print("No tasks found. The to-do list is empty.")
    except Exception as e:
            logging.error(f"An error occurred while reading tasks: {e}")
            print("An error occurred while reading the tasks.")

def write_tasks():
    try:
        with open(file_path, 'w') as file:
             file.writelines(task + '\n' for task in task_list)
    except FileNotFoundError:
            logging.error("The to-do list file was not found.")
            print("Error: The to-do list file was not found.")
    except Exception as e:
            logging.error(f"An error occurred while writing tasks: {e}")
            print("An error occurred while writing the tasks.")

def view_tasks():
    if not task_list:
        print("No tasks found. The to-do list is empty.")
        logging.info("The to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task.strip()}")

def add_task(task):
    task_list.append(task)
    write_tasks()
    logging.info(f"Task added successfully: {task.strip()}")


def remove_task(task):
    task_to_remove = task
    if task_to_remove in task_list:
        task_list.remove(task_to_remove)
        write_tasks()
        logging.info(f"Task removed successfully: {task.strip()}")
    else:
        logging.warning(f"Task not found: {task.strip()}")
        print("Task not found in the to-do list.")

# Main program loop

display_menu()

while True:
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        read_tasks()
        view_tasks()
    elif choice == '3':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


