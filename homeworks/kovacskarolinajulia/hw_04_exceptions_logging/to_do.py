import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("to_do.log", encoding="utf-8")
    ]
)


def read_tasks():
    tasks = []

    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        logging.info("A feladatok beolvasasa sikerult.")
    except FileNotFoundError:
        logging.warning("A tasks.txt fajl nem talalhato.")
    except OSError as error:
        logging.error("Hiba a fajl olvasasakor: %s", error)

    return tasks


def write_tasks(tasks):
    try:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        logging.info("A feladatok mentese sikerult.")
    except OSError as error:
        logging.error("Hiba a fajl irasakor: %s", error)


def view_tasks(tasks):
    if len(tasks) == 0:
        print("Nincsenek feladatok.")
    else:
        print("\nFeladatok:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def add_task(tasks, task):
    tasks.append(task)
    logging.info("Uj feladat hozzaadva: %s", task)
    print("A feladat hozzaadva.")


def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        logging.info("Feladat torolve: %s", task)
        print("A feladat torolve.")
    else:
        print("Ez a feladat nem talalhato a listaban.")
        logging.warning("Nem talalhato torlendo feladat: %s", task)


def display_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    tasks = read_tasks()

    while True:
        display_menu()
        choice = input("Valassz egy opciot (1-4): ").strip()

        if choice == "1":
            task = input("Add meg az uj feladatot: ").strip()
            if task:
                add_task(tasks, task)
            else:
                print("A feladat neve nem lehet ures.")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            if len(tasks) == 0:
                print("Nincs mit torolni.")
            else:
                view_tasks(tasks)
                task = input("Ird be a torlendo feladat pontos nevet: ").strip()
                remove_task(tasks, task)

        elif choice == "4":
            write_tasks(tasks)
            print("Viszlat!")
            break

        else:
            print("Ervenytelen valasztas. Valassz 1, 2, 3 vagy 4 kozul.")
            logging.warning("Ervenytelen menupont: %s", choice)


if __name__ == "__main__":
    main()

