import random


def play_game():
    target = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess (1-100): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if guess < target:
            print("Too low.")
        elif guess > target:
            print("Too high.")
        else:
            print("Correct!")
            return


if __name__ == "__main__":
    play_game()
