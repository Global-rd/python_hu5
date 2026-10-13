import os
from pathlib import Path
import logging
import rp_logging_setup as rls

 # Logger setup

rls.setup_logging()
logger = logging.getLogger()

def read_tasks(file_path):
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            tasklist = list(map( lambda x : x.strip(),  file.readlines()))
            # print(tasklist)
            return tasklist
    except Exception as e:
        logger.error(f'Could not open file: {e}')
        return []
                
def write_tasks(tasklist, file_path):    
    try:
        with open(file_path, "w", encoding='utf-8') as file:
            file.write('\n'.join(tasklist))
    except Exception as e:
        logger.error(f'Could not write to file: {e}')
    
def display_tasks(tasklist):
    for task in tasklist:
        print(task.strip())

def remove_task(task, tasklist):
    try:
        tasklist.remove(task)
    except ValueError as ve:        
        logger.info(f'{task}: There is no such task')

def add_task(task, tasks):
    tasks.append(task)
    
def display_menu():
    menuitems=['Add Task', 'View Tasks', 'Remove Task', 'Exit']
    for i, menuitem in enumerate(menuitems, 1):
        print(i, menuitem)

def main():
    print(os.getcwd())
    script_dir = Path(__file__).resolve().parent 

    file_path = script_dir /"tasks.txt"
    
    invalid_choice_msg='Invalid choice. Please enter 1,2,3, or 4!'
    tasklist = read_tasks(file_path)
    
    display_tasks(tasklist)
    while True: 
        display_menu()
        try:       
            choice = int(input('Your choice: '))
        
            if choice == 1:  
                new_task=input('Enter new task: ')              
                add_task(new_task, tasklist)
            elif choice == 2:
                display_tasks(tasklist)
            elif choice == 3:
                task_to_remove = input('Enter task to be removed: ')
                remove_task(task_to_remove, tasklist)
            elif choice == 4:
                write_tasks(tasklist, file_path)
                return
            else:              
                logger.info(invalid_choice_msg)
        except ValueError as ve:
            
            logger.error( str(ve) + ' - ' + invalid_choice_msg)
    
main()
