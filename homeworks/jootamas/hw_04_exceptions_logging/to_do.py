"""
Hozz létre egy to_do.py nevű file-t, és kódold le a következő feladat megoldását:
Készíts egy Feladatkezelő alkalmazást!
- Definiálj 5 függvényt a következőkre: feladatok olvasása, feladatok
írása, feladatok megjelenítése, egy feladat hozzáadása, egy feladat
törlése
- Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges
opciókat:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok
közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt.
A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! Ha az 1-es
vagy 3-as opciót választja, mindkét esetben paramétert kell átadnod a
megfelelő függvénynek. “Exit”-re lépjen ki a program.
Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd a
logging module-t. Egyszerre logolj a konzolra és egy .log file-ba. A .txt file
legyen része a pull request-nek.
Tipp:
A program futása során a feladatokat memóriában (egy listában) tartsd
nyilván (itt adj hozzá vagy törölj elemeket a function hívásoknál).
A file-ból való olvasás automatikusan történjen meg a program indulásakor. A
fájlba írás csak a program befejezésekor (“Exit” opció választásakor)
történjen meg, ekkor a program írja felül a korábbi feladatlistát a módosított
tartalommal (nem kell minden Add Task vagy Remove Task opciónál
módosítani a file-t).
"""

from pathlib import Path
import logging

# ezt nem vettuk, csak utananeztem, igy barhonnan futtatva a script mappajabol olvassa es hozza letre a file-t
tasks_file_path = f"{Path(__file__).resolve().parent}/tasks.txt"

tasks = []

# logging
logging_file_handler = logging.FileHandler("tasks.log")
logging_stream_handler = logging.StreamHandler()
logging_file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logging_stream_handler.setFormatter(logging.Formatter("%(message)s")) # usernek eleg csak az uzenet
logging_file_handler.setLevel(logging.DEBUG)
logging_stream_handler.setLevel(logging.INFO) # usernek eleg csak az info
logger = logging.getLogger()
logger.addHandler(logging_file_handler)
logger.addHandler(logging_stream_handler)
logger.setLevel(logging.DEBUG)

def read_tasks():
  # a global-rol volt szo Discordon, hogy inkabb kerulendo,
  # de itt a feladat kulon fuggvenyben keri a beolvasast es feltoltest
  global tasks

  try:
    with open(tasks_file_path, "r") as file:
      lines = file.readlines()
      # ne maradjon a feladatok vegen a newline, mert felesleges
      # es file-ba visszairaskor is kap newline-t, ami dupla newline-t, azaz ures sorokat eredmenyezne
      tasks = list(map(lambda s: s.strip(), lines))
      logger.debug("A tasks.txt sikeresen beolvasva")
  except FileNotFoundError:
    # nincs teendo, mert nincs meg feladatlista, marad uresen a tasks es az iras a vegen letrehozza
    pass
  except Exception:
    logger.error("A tasks.txt beolvasása sikertelen")
    # kilepunk, mert a file nelkul nincs ertelme futtatni a programot
    exit()

def write_tasks():
  try:
    with open(tasks_file_path, "w") as file:
      for task in tasks:
        file.write(f"{task}\n")
      logger.debug("A tasks.txt sikeresen frissítve")
      return True
  except Exception:
    logger.error("A tasks.txt írása sikertelen!")
    return False

def show_tasks():
  print("----- Jelenlegi feladataid -----")
  if tasks:
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")
  else:
    print("Nincs még egy feladatod sem!")
  print("----------")

def add_task(task):
  tasks.append(task)

def remove_task(task_index):
  tasks.pop(task_index)

def display_menu():
  print("----- Menü -----")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Remove Task")
  print("4. Exit")
  print("----------")

def main():

  logger.debug("Program elindítva")

  # beolvassuk a feladatokat
  read_tasks()

  while True:
    display_menu()
    selected_option = input("Kérlek add meg mit szeretnél csinálni (1-4): ").strip()
    if not(selected_option.isdigit()):
      print("A megadott érték nem szám, kérlek próbáld újra!")
    elif int(selected_option) not in [1, 2, 3, 4]:
      print("Csak 1-4 opció választható!")
    else:
      selected_option = int(selected_option)

      if selected_option == 1:
        while True:
          task = input("Kérlek add meg az új feladatot: ").strip()
          if task:
            add_task(task)
            logger.info(f"A feladat sikeresen hozzáadva: {task}")
            break

      if selected_option == 2:
        show_tasks()

      if selected_option == 3:
        tasks_length = len(tasks)

        if tasks_length == 0:
          print("Nincs még egy feladatod sem, nincs mit törölni!")
          continue

        show_tasks()

        while True:
          remove_task_number = input("Kérlek add meg a törlendő feladat sorszámát: ")
          if not remove_task_number.isdigit():
            print("A megadott érték nem pozitív egész szám, kérlek próbáld újra!")
            continue
          if int(remove_task_number) == 0:
            print("A nulladik feladat nem értelmezhető, próbáld újra!")
            continue
          if tasks_length < int(remove_task_number):
            print(f"A feladatlistád csak {tasks_length} elemű, próbáld újra!")
            continue
          break

        remove_task_number = int(remove_task_number)
        removed_task = tasks[remove_task_number-1]
        remove_task(remove_task_number-1)
        logger.info(f"A feladat sikeresen törölve: {removed_task}")

      if selected_option == 4:
        if write_tasks():
          logger.debug("Program bezárva")
          break

main()
