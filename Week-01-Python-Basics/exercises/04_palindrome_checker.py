def is_palindrome(value):
    normalized = "".join(value.lower().split())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    print("Palindrome" if is_palindrome(input("Enter text: ")) else "Not a palindrome")
