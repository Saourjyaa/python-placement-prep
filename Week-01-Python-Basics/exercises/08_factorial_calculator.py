def factorial(number):
    if number < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


if __name__ == "__main__":
    try:
        print(factorial(int(input("Enter a non-negative integer: "))))
    except ValueError as error:
        print(error)
