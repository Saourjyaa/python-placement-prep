def is_armstrong(number):
    if number < 0:
        return False
    digits = str(number)
    return sum(int(digit) ** len(digits) for digit in digits) == number


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print("Armstrong number" if is_armstrong(number) else "Not an Armstrong number")
    except ValueError:
        print("Please enter a whole number.")
