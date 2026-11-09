import json
from pathlib import Path


def demonstrate(path=None):
    file_path = Path(path) if path else Path(__file__).with_name("sample.json")
    data = {"name": "Aarav", "skills": ["Python", "Git"]}
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    with file_path.open("r", encoding="utf-8") as file:
        loaded = json.load(file)
    loaded["skills"].append("Testing")
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(loaded, file, indent=2)
    print(loaded)


if __name__ == "__main__":
    demonstrate()
