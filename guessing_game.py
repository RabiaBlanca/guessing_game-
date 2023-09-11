import random
import sys
import re

print("-GUESSING GAME- \n")
def profile_user():
    while True:
        user_name = input("Username: ")
        pattern1 = r"(?i)[^a-z0-9_><]"
        pt = re.compile(pattern1)
        if refa := re.findall(pt, user_name):
            print("you can not use punctuations.")

        elif len(user_name) < 3:
            print(f"Not valid username. \n")
        else:
            print(f"Mr. {user_name}, hope you having a great day.")
            break


def main_game():
    profile_user()
    random_number = random.randint(1, 30)
    chances = 5

    while True:
        try:
            user_guess = int(
                input(
                    f"\nEnter a number between (1, 30), You have - {chances} - chances: "
                )
            )

            match user_guess:
                case ug if ug < 1 or ug >= 31:
                    print("\ninvalid number, try again.")

                case ug if ug == random_number:
                    print(f"\nRight guess!, You win.")

                    play_again()
                    break

                case ug if ug > random_number:
                    print(
                        f"\nLower, try again. You have - {chances - 1} - chances left."
                    )
                    chances -= 1

                case ug if ug < random_number:
                    print(
                        f"\nHigher. Try again. You have - {chances - 1} - chances left."
                    )
                    chances -= 1

            if chances == 0:
                print(f"\nYou lose, the number was {random_number}.")
                play_again()

        except ValueError:
            print("\nPlease enter a number.")


def play_again():
    while True:
        print("\nDo you want to play again?")
        play_again = input("(Yes, No): ").capitalize()
        if play_again == "Yes":
            main_game()
        else:
            sys.exit("\nThanks for playing, Have a great day.")


if __name__ == "__main__":
    main_game()
