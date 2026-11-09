def count_words(text):
    return len(text.split())


if __name__ == "__main__":
    print(count_words(input("Enter a sentence: ")))
