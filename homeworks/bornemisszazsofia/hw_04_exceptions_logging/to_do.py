import logging
from pathlib import Path

# Logging config:

log_path = Path(__file__).parent / "to_do.log"

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(log_path)
        ],
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Functions library:

task_list_path = Path(__file__).parent / "to_do_list.txt"
task_list =[]

def display_menu():
    print(f"Please select an option: 1. Add a task / 2. View tasks / 3. Remove a task / 4. Exit. ")

def reading_task(task_list):
    try:
        with open(task_list_path, "r") as f:
            for task in f:
                task = task.strip()
                task_list.append(task)
        logging.info(f"Tasks successfully loaded from '{task_list_path}'.")
    except FileNotFoundError:
        print("The file does not exist.")
        logging.warning("The file you want to read does not exist.")

def writing_task(task_list):
    try:
        with open(task_list_path, "w") as f:
            for task in task_list:
                f.write(task + "\n")
        logging.info("Tasks saved successfully.")
    except PermissionError:
        print("Unable to save tasks due to insufficient permissions.")
        logging.error("Unable to save tasks: permission denied.")
    except FileNotFoundError:
        print("Unable to save tasks: destination folder does not exist.")
        logging.error("Unable to save tasks: destination folder does not exist.")

def view_task(task_list):
    if task_list == []:
        print("No tasks to display.")
        logging.info("No values to display.")
    else:
        for task in task_list:
            print(task)

def add_task(task):
    task_list.append(task)
    logging.info(f"Task '{task}' added successfully.")


def remove_task(task):
    try:    
        task_list.remove(task)
        logging.info(f"Task '{task}' removed successfully.")
    except ValueError:
        print("Task not found.")
        logging.warning(f"Task '{task}' does not exist.")


# Main program:

display_menu()
reading_task(task_list)
#print(task_list)

option_choice = 0
while option_choice != 4:
    try:   
        option_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a number between 1 and 4: ")
        logging.warning("Invalid input.")
        continue

    if option_choice not in [1, 2, 3, 4]:
        print("Enter a number between 1 and 4: ")
        logging.warning("Invalid input.")
        continue
    logging.info(f"Valid menu option {option_choice} selected.")

    if option_choice == 1:
        task = input("Please enter the task you'd like to add. ").strip() 
        if task == "":
            print("Task cannot be empty.")
            logging.warning("Empty space entered.")
        else:
            add_task(task)
    elif option_choice == 2:
        view_task(task_list)
    elif option_choice == 3:
         task = input("Please enter the task you'd like to remove. ").strip()
         remove_task(task)
    
writing_task(task_list)
logging.info("Application closed.")






