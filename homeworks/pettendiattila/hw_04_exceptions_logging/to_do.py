import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", encoding="utf-8")

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

def display_menu() -> None:
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def read_tasks(file_path: Path) -> list:
    tasks = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        logger.info(f"Feladatok sikeresen betöltve: {len(tasks)} db feladat.")
    except FileNotFoundError:
        logger.warning(f"{file_path} fájl még nem létezik. Új üres lista indul.")
    except Exception as e:
        logger.error(f"Hiba történt a fájl olvasásakor: {e}")

    return tasks


def display_tasks(tasks: list) -> None:
    if not tasks:
        print("Nincsenek feladatok a listában.")
        return

    print("\n--- AKTUÁLIS FELADATOK ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("--------------------------\n")


def add_task(tasks: list, new_task: str) -> None:
    cleaned_task = new_task.strip()
    if not cleaned_task:
        print("Hiba: Üres feladatot nem lehet hozzáadni!")
        logger.warning("Sikertelen hozzáadás: üres feladatszöveg.")
        return

    tasks.append(cleaned_task)
    print(f"Feladat sikeresen hozzáadva: {cleaned_task}")
    logger.info(f"Új feladat hozzáadva: {cleaned_task}")


def remove_task(tasks: list, task_index: int) -> None:
    try:
        if task_index < 1:
            raise IndexError("A feladat sorszáma nem lehet 1-nél kisebb!")
        
        removed_task = tasks.pop(task_index - 1)
        print(f"Feladat sikeresen törölve: {removed_task}")
        logger.info(f"Feladat törölve sorszám: {task_index}: {removed_task}")
    except IndexError as e:
        print(f"Hiba: Érvénytelen sorszám! {e}")
        logger.warning(f"Sikertelen törlés érvénytelen sorszám miatt {task_index}: {e}")


def write_tasks(file_path: Path, tasks: list) -> None:
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task}\n")
        logger.info(f"Feladatok sikeresen elmentve {file_path} fájlba ({len(tasks)} db).")
    except Exception as e:
        logger.error(f"Hiba történt a fájl mentésekor: {e}")


def main() -> None:
    file_path = Path(__file__).resolve().parent / "tasks.txt"
    tasks = read_tasks(file_path)

    while True:
        display_menu()
        choice = input("Válassz egy menüpontot (1-4): ").strip()

        if choice == "1":
            new_task = input("Add meg az új feladatot: ")
            add_task(tasks, new_task)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            try:
                task_index = int(input("Add meg a törölni kívánt feladat sorszámát: "))
                remove_task(tasks, task_index)
            except ValueError:
                print("Hiba: Egész számot adj meg!")
                logger.warning("Érvénytelen bemenet (nem szám).")
        elif choice == "4":
            write_tasks(file_path, tasks)
            print("Kilépés... Viszlát!")
            logger.info("Az alkalmazás sikeresen leállt.")
            break
        else:
            print("Hiba: Érvénytelen választás! Csak 1, 2, 3 vagy 4 adható meg.")
            logger.warning(f"Érvénytelen menüválasztás történt: {choice}")


if __name__ == "__main__":
    main()