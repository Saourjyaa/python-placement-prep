import json
from pathlib import Path


class StorageError(Exception):
    """Raised when expense storage cannot be read or written."""


def load_expenses(path):
    file_path = Path(path)
    if not file_path.exists():
        return []
    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        raise StorageError(f"Could not read {file_path}: {error}") from error
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise StorageError("Expense data must be a JSON list of objects.")
    return data


def save_expenses(path, expenses):
    file_path = Path(path)
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=2)
            file.write("\n")
    except OSError as error:
        raise StorageError(f"Could not write {file_path}: {error}") from error
