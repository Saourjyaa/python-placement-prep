from pathlib import Path


def demonstrate(path=None):
    file_path = Path(path) if path else Path(__file__).with_name("sample.txt")
    try:
        with file_path.open("r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    with file_path.open("a", encoding="utf-8") as file:
        file.write("\nAppended line.")
    with file_path.open("r", encoding="utf-8") as file:
        print(file.read())


if __name__ == "__main__":
    demonstrate()
