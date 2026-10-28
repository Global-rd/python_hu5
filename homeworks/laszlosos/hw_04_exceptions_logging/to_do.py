from pathlib import Path #fajl eleresi utvonal 
import logging #logger importalasa 

file_path = Path( "homeworks" ) / "laszlosos" /  "hw_04_exceptions_logging" / "tasks.txt" #txt file eleresi ut, az altalanos formatum hasznalata ami mas operacios rendszereken is mukodik

log_path = Path( "homeworks" ) / "laszlosos" /  "hw_04_exceptions_logging" / "to_do.log" #logger eleresi utjanak letrehozasa 
file_handler = logging.FileHandler(log_path)
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG)

#function-ok definialas 

#kiirja a feladatrok listajat a fajlba
def write_tasks(tasks):
    try: #hibakezeles
        with open(file_path, "w") as file: #write mode
            for task in tasks: #for loop kell, mert a lista elemein egyesevel akarunk vegigmenni
                file.write(task + "\n") #\n linebreak, a lista elemeit kulon sorba akrjuk kiirni 
    except Exception as e:
        logger.error(f"Error while saving: {e}") #nem tudjuk pontosan milyen hiba tortenik, igy az altalanos formula. Print helyett pedig log 

def read_tasks(): #feladatok beolvasasa a fajlbol, listakent adja vissza
    tasks = [] # ureslista letrehozasa, ebben taroljuk el a feladatokat 
    try: #hibakezeles
        with open(file_path, "r") as file: #tasks.txt megnyitasa read modeban, a with automatikusan bezarja 
            for line in file: #for loop kell, soronkent olvassuk a txt file-t 
                tasks.append(line.strip()) #strip a \n eltavolitasara, majd a tisztitott szoveg hozzaadasa a listahoz 
    except FileNotFoundError: #error code a hianyzo fajlra 
        logger.warning("Error, file not found!")
    return tasks # kesz lista visszaadasa a mainnek

def view_tasks(tasks):
    for task in tasks:
        print(task) #vegigmegy a taskokon es egyesevel kiirja

def add_a_task(tasks, task): 
    tasks.append(task)


def remove_a_task(tasks, task):
    tasks.remove(task)
#menu kiirasa
def display_menu():
    print("1: Add Task")
    print("2: View Tasks")
    print("3: Remove Task")
    print("4: Exit")

#program fo resze, innen fog indulni minden 
def main():
    logger.info("Program started")
    tasks = read_tasks() #read function meghivasa a program indulasakor
    while True: #loop a feladatok bekeresere 
        display_menu()
        chosen_option = input("Choose an option: ")
        if chosen_option == "1":
            new_task = input("Enter a task: ")
            add_a_task(tasks, new_task) #new task hozzaadasa a fenti listahoz amit a felhasznalo az 1-es opcional ad meg 
        elif chosen_option == "2":
                view_tasks(tasks) #meghivja a fent definialt view_tasks fuggvenyt 
        elif chosen_option == "3":
            removed_task = input("Enter a task: ")
            remove_a_task(tasks, removed_task) #a fent beirt task eltavolitasa 
        elif chosen_option == "4":
            write_tasks(tasks) #write fuggveny meghivasa 
            break #amikor 4-est valaszt a felhasznalo a program kilep 
        else:
            print("Choice is invalid")

main()

