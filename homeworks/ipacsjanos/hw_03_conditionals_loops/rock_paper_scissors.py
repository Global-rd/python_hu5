# 1. LÉPÉS: Páratlan körök számának bekérése validálással
total_rounds = 0
while True:
    try:
        total_rounds = int(input("Hány kört szeretnétek játszani? (Páratlan számot adj meg): "))
        if total_rounds % 2 != 0 and total_rounds > 0:
            break
        print("Hiba: Csak pozitív páratlan számot adhatsz meg, különben döntetlen lehet a vége!")
    except ValueError:
        print("Hiba: Kérlek, érvényes számot adj meg!")

# Pontszámok nyomon követése
p1_score = 0
p2_score = 0
current_round = 1

# 2. LÉPÉS: A játékmenet vezérlése a teljes meccsszámig
while current_round <= total_rounds:
    print(f"\n--- {current_round}. KÖR ---")
    
    # 1. Játékos döntésének bekérése validálással
    while True:
        p1_choice = input("1. Játékos tippje (rock/paper/scissors): ").strip().lower()
        if p1_choice in ["rock", "paper", "scissors"]:
            break
        print("Hiba: Csak 'rock', 'paper' vagy 'scissors' adható meg!")
        
    # 2. Játékos döntésének bekérése validálással
    while True:
        p2_choice = input("2. Játékos tippje (rock/paper/scissors): ").strip().lower()
        if p2_choice in ["rock", "paper", "scissors"]:
            break
        print("Hiba: Csak 'rock', 'paper' or 'scissors' adható meg!")

    # Kör eredményének kiértékelése
    if p1_choice == p2_choice:
        print("Döntetlen ebben a körben! Ezt a kört újrajátsszátok.")
        continue  # A 'continue' miatt a ciklus újraindul, current_round nem növekszik
        
    # Nyertes meghatározása
    p1_wins = (
        (p1_choice == "rock" and p2_choice == "scissors") or
        (p1_choice == "paper" and p2_choice == "rock") or
        (p1_choice == "scissors" and p2_choice == "paper")
    )
    
    if p1_wins:
        print("Az 1. Játékos nyerte ezt a kört!")
        p1_score += 1
    else:
        print("A 2. Játékos nyerte ezt a kört!")
        p2_score += 1
        
    current_round += 1  # Sikeres kör végén növeljük a kör számlálót

# 3. LÉPÉS: Végeredmény hirdetése
print("\n=============================")
print("JÁTÉK VÉGE - VÉGEREDMÉNY")
print(f"Állás: 1. Játékos: {p1_score} pont | 2. Játékos: {p2_score} pont")

if p1_score > p2_score:
    print(f"A játékot az 1. JÁTÉKOS nyerte {p1_score} ponttal!")
else:
    print(f"A játékot a 2. JÁTÉKOS nyerte {p2_score} ponttal!")
