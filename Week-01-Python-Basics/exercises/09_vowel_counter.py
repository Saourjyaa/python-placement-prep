def count_vowels(text):
    return sum(character.lower() in "aeiou" for character in text)


if __name__ == "__main__":
    print(count_vowels(input("Enter text: ")))
