def read_number():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        result = first / second
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("The second number cannot be zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Calculation finished.")


if __name__ == "__main__":
    read_number()
