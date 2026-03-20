import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def print_rows(row):
    print(" ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 6
        elif row[0] == '⭐':
            return bet * 10
    else:
        return 0


def main():
    balance = 100

    print("*****************************")
    print("  Welcome to python slot  ")
    print("  symbols: 🍒 🍉 🍋 🔔 ⭐  ")
    print("*****************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("place your bet amount: ")

        if not bet.isdigit:
            print("Please enter a valid number")
            return 0

        bet = int(bet)

        if bet > balance:
            print("Insufficient funnds")
            continue

        if bet <= 0:
            print("Invalid bet")
            continue

        balance -= bet

        row = spin_row()
        print("spinning....\n")
        print_rows(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print("**********************************")
            print(f"Congratulations you won ${payout}")
            print("**********************************")
        else:
            print("Sorry you lost this round")

        balance += payout

        should_continue = input("would you like continue (y or n)?: ").lower()
        if should_continue == "n":
            break

    print("********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")


if __name__ == "__main__":
    main()
