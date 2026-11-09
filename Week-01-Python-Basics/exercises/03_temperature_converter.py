def celsius_to_fahrenheit(value):
    return value * 9 / 5 + 32


def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9


if __name__ == "__main__":
    try:
        value = float(input("Temperature: "))
        unit = input("Unit (C/F): ").strip().upper()
        if unit == "C":
            print(f"{celsius_to_fahrenheit(value):.2f} F")
        elif unit == "F":
            print(f"{fahrenheit_to_celsius(value):.2f} C")
        else:
            print("Unit must be C or F.")
    except ValueError:
        print("Please enter a valid number.")
