""" 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
HW 03 - Feladat 1. (if-elif-else, operátorok)
by Kiss Tibor
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

# ADDIG KÉRÜNK BE ADATOT, AMÍG A BÉRLETI DÍJ ELFOGADHATÓ NEM LESZ.
while True:
    input_data = input("Add meg a bérleti díj összegét: ")

    # A SZÁMJEGYVIZSGÁLATHOZ ELTÁVOLÍTJUK A SZÉLSŐ SZÓKÖZÖKET, A KEZDŐ MÍNUSZJELEKET,
    # VALAMINT A TIZEDESPONTOT 
    input_in_digits = input_data.strip().lstrip('-').replace('.', '', 1)

    # Üres értéket és önmagában megadott előjelet/tizedespontot nem fogadunk el.
    if not (input_in_digits.isdigit() and input_data not in ('', '-', '.')):
        print("Érvénytelen a beírt szám! Próbáld meg újra!")   

    else:
        # AMENNYIBEN A TISZTÍTOTT INPUT VÁLTOZÓ CSAK SZÁMOKAT TARTALMAZ,
        # AKKOR AZ EREDTI INPUTOT BETÁROLJUK FLOAT TÍPUSÚ ADATKÉNT A TOVÁBBI ÖSSZEHASONLÍTÁSOKHOZ.
        rent_cost= float(input_data)

        # POZITÍV BÉRLETI DÍJ ESETÉN ELFOGADJUK AZ ÉRTÉKET ÉS KILÉPÜNK A CIKLUSBÓL.
        if rent_cost> 0:
            break

        # NEGATÍV ÖSSZEGET NEM FOGADUNK EL; ÚJRA BEKÉRJÜK A BÉRLETI DÍJAT.
        else:
            print("Kérlek pozitív összeget írj ! ")


# FELHASZNÁLÓ ÁLTAL MEGADOTT BÉRLETI DÍJ MEGJELENÍTÉSE
print("---------------------------------------")
print(F"MEGADOTT BÉRLETI DÍJ: ${rent_cost}. ")
print("---------------------------------------")
print(" ")

#VÁROS BEKÉRÉSE ÉS TISZTÍTÁSA - SZÓKÖZÖK ELTÁVOLÍTÁSA ÉS A KEZDŐBETŰK NAGYBETŰSÍTÉSE
city = (input("Adj meg egy várost: ")).title().strip()  

# FELHASZNÁLÓ ÁLTAL MEGADOTT VÁROS MEGJELENÍTÉSE
print("---------------------------------------")
print(F"MEGADOTT VÁROS: {city.upper()}. ")
print("---------------------------------------")
print(" ")

#VALIDÁLHATÓ VÁROCSOPORTOK A KÖLTÖZÉSI DÖNTÉSHEZ.
hate_cities         = ["Washington"]
like_cities         = ["New York", "San Fransisco"]
very_like_cities    = ["Chicago"]

# DÖNTÉS KIÉRTÉKELÉSE
if city in hate_cities:
    decision_var = False

elif city in very_like_cities:
    decision_var = True

# A KEDVELT VÁROSOKNÁL LEGFELJEBB 4000-ES BÉRLETI DÍJ ENGEDÉLYEZETT.
elif city in like_cities:     
     decision_var = rent_cost<= 4000

# MÁS VÁROSOKNÁL CSAK 3000 ALATTI BÉRLETI DÍJ ESETÉN KÖLTÖZHET.
else:    
    decision_var = rent_cost< 3000

# A LOGIKAI DÖNTÉST SZÖVEGES VÁLASSZÁ ALAKÍTJUK.
answer = "költözni tud" if decision_var else "nem fog költözni"

# KIÍRÁS - SARAH KÖLTÖZÉSI LEHETŐSÉGE A MEGADOTT VÁROSBAN.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(F"Sarah {answer} {city} városba.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
