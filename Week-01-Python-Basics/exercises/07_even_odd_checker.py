if __name__ == "__main__":
    try:
        number = int(input("Enter an integer: "))
        print("Even" if number % 2 == 0 else "Odd")
    except ValueError:
        print("Please enter a whole number.")
