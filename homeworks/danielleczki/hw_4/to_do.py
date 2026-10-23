import logging

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("to_do.log", encoding="utf-8")
    ]
)

def feladatok_olvasasa():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as fajl:
            feladatok = fajl.readlines()

        feladatok = [
            feladat.strip()
            for feladat in feladatok
            if feladat.strip()
        ]

        logging.info("A feladatok sikeresen beolvasva!")
        return feladatok
    except FileNotFoundError:
        logging.info("Még nem létezik a feladatfájl. Üres listával indultunk. ")
        return []
    except OSError:
        logging.exception("Hiba történt a feladatok beolvasásakor! ")
        return []

def feladatok_irasa(feladatok):
    try:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for feladat in feladatok:
                file.write(feladat + "\n")
        logging.info("A fájl sikeresen elmentve! ")

    except OSError:
        logging.exception("Hiba történt a feladatok mentésekor! ")
    
def feladatok_megjelenitese(feladatok):
    if not feladatok:
            print("Nincsenek feladatok! ")
            return

    print("\n ------Feladataim--------")

    for sorszam, feladat in enumerate(feladatok, start=1):
        print(f"------{sorszam}, {feladat}-------")

def feladatok_hozzaadasa(feladatok, uj_feladat):
    uj_feladat = uj_feladat.strip()

    if not uj_feladat:
        print("A feladat nem lehet üres!")
        return

    feladatok.append(uj_feladat)
    logging.info("Új feladat hozzáadva: %s", uj_feladat)
    print("Feladat hozzáadva.")

def feladat_torlese(feladatok, sorszam):
    if not sorszam.isdigit():
        print("Hibás sorszámot adtál meg. ")
        return

    sorszam = int(sorszam)

    if sorszam < 1 or sorszam > len(feladatok):
        print("Nincs ilyen sorszámú feladat!")
        return

    torolt_feladat = feladatok.pop(sorszam -1)
    logging.info("A feladat törölve: %s", torolt_feladat)
    print(f"Törölve: {torolt_feladat}")

def display_menu():
    print("\n ---Feladatkezelő---")
    print("1. Add Task")
    print("2 View Tasks")
    print("3 Remove Task")
    print("4 Exit")

def main():
    feladatok = feladatok_olvasasa()

    logging.info("A program elindult!")

    while True:
        display_menu()
        valasztas = input("Válassz menüpontot (1-4): ").strip()

        if valasztas == "1":
            uj_feladat = input("Add meg az új feladatot: ")
            feladatok_hozzaadasa(feladatok, uj_feladat)
        elif valasztas == "2":
            feladatok_megjelenitese(feladatok)
        elif valasztas == "3":
            feladatok_megjelenitese(feladatok)
            if feladatok:
                sorszam = input("Melyik sorszámú feladatot töröljem? ")
                feladat_torlese(feladatok, sorszam)
        elif valasztas == "4":
            feladatok_irasa(feladatok)
            logging.info("A program leállt. ")
            print("A program kilép. A feladatok mentése megtörtént. ")
            break

if __name__ == "__main__":
    main()