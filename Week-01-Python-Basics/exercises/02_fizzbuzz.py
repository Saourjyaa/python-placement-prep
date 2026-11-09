def fizzbuzz(start, end):
    for number in range(start, end + 1):
        result = ""
        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        print(result or number)


if __name__ == "__main__":
    try:
        start = int(input("Start: "))
        end = int(input("End: "))
        fizzbuzz(start, end)
    except ValueError:
        print("Please enter whole numbers.")
