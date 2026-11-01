


def get_odd_round_count():
    while True:
        try:
            rounds = int(input("Hány kört szeretnétek játszani? "))
            if rounds > 0 and rounds % 2 == 1:
                return rounds
            print("Hiba: pozitív, páratlan számot adj meg!")
        except ValueError:
            print("Hiba: egész számot adj meg!")


def get_choice(player):
    valid_choices = ("rock", "paper", "scissors")

    while True:
        choice = input(
            f"{player}, válassz (rock, paper, scissors): "
        ).strip().lower()

        if choice in valid_choices:
            return choice

        print("Érvénytelen választás. Írd be: rock, paper vagy scissors.")


def round_winner(choice1, choice2):
    if choice1 == choice2:
        return None

    if (
        (choice1 == "rock" and choice2 == "scissors")
        or (choice1 == "paper" and choice2 == "rock")
        or (choice1 == "scissors" and choice2 == "paper")
    ):
        return 1

    return 2


def main():
    rounds_to_play = get_odd_round_count()
    player1_score = 0
    player2_score = 0
    completed_rounds = 0

    while completed_rounds < rounds_to_play:
        print(f"\n{completed_rounds + 1}. kör")

        player1_choice = get_choice("1. játékos")
        player2_choice = get_choice("2. játékos")

        winner = round_winner(player1_choice, player2_choice)

        if winner is None:
            print("Döntetlen! Ezt a kört újra kell játszani.")
            continue

        completed_rounds += 1

        if winner == 1:
            player1_score += 1
            print("Az 1. játékos nyerte a kört.")
        else:
            player2_score += 1
            print("A 2. játékos nyerte a kört.")

        print(
            f"Állás: 1. játékos {player1_score} – "
            f"{player2_score} 2. játékos"
        )

    print("\nVégeredmény:")

    if player1_score > player2_score:
        print(f"Az 1. játékos nyert {player1_score} ponttal.")
    else:
        print(f"A 2. játékos nyert {player2_score} ponttal.")

    print(
        f"Pontok: 1. játékos {player1_score}, "
        f"2. játékos {player2_score}"
    )


if __name__ == "__main__":
    main()

