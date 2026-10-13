import logging
import os
print(os.getcwd())

#--------logging-----------

logging.basicConfig(
    filename="homework.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
#--------global parameters-------

file_path = r"C:\Users\user\Documents\Python kezdőknek\python_hu5\homeworks\nadudvarivirag\hw_04_exceptions_logging\homework.txt"
tasks_list = []

#-------defining program functions-------

# 1. read tasks
def read_tasks():
    try:
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file]
            return lines
    except FileNotFoundError:
        logging.error("The directory does not exist at the specified path.")
        print("The directory does not exist at the specified path.")
        return []

# 2. write task 
def write_tasks():
    try:
        with open(file_path, "w") as file:
            for task in tasks_list:
                file.write(task + "\n")
        logging.info("Tasks saved successfully.")
        print("Tasks saved successfully")
    except FileNotFoundError:
            logging.error("Directory not found while saving tasks")
            print("The directory does not exist at the specified path.")

# 3. view tasks
def view_tasks():
    print('--------------')
    print("The task list:")

    for index, tasks in enumerate(tasks_list, start=1):
        print(f"{index}. {tasks.strip()}")
    print("--------------")

# 4. add tasks
def add_tasks(add_text):
    tasks = add_text.split(",")
    
    for task in tasks:
        tasks_list.append(task.strip())
    print("The tasks are appended to the to do list")

# 5. remove tasks
def remove_tasks(remove_text): 
    view_tasks()
    if remove_text not in tasks_list:
        print("The task is not found!")
        return

    tasks_list.remove(remove_text)
    print("The task is removed.")
 
# 6. exit from the program
def exit_program():
    print("Exit from the program")
    return

# display menu for the users
def display_menu():
    print('-----------------')
    print("You can choose from the following options:")
    for task in ("1. Add Task", "2. View Tasks", "3. Remove Task", "4. Exit"):
        print(task)
    print("-----------------")

# A program indulása


tasks_list = read_tasks()


while True:
    display_menu()
    try:
        task_choice = int(input("Choose an option from 1 to 4: "))
        print("-----------")
    except ValueError:
        print("Please give me a number!")
        continue
    
    if task_choice == 1:
        add_text = input("Write the new task: ").strip()
        add_tasks(add_text)  
    elif task_choice == 2:
        view_tasks()
    elif task_choice == 3:
        view_tasks()
        remove_text = input("What task would you like to remove: ").strip()
        remove_tasks(remove_text)
    elif task_choice == 4:
        exit_program()
        write_tasks()
        break
    else:
        print("You have to choose a number from 1 to 4:")
