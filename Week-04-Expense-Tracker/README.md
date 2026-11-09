# Week 4: CLI Expense Tracker

## Project overview

This project is a small command-line expense tracker. It stores expenses persistently in `expense_tracker/data/expenses.json` and supports adding, listing, totaling, and deleting records.

## Features and technologies

The application uses Python, `argparse`, JSON, and pytest. Each expense has an automatically generated ID, description, positive amount, category, and date (today by default). Missing storage is treated as an empty list; malformed storage is reported clearly.

## Installation

From the repository root:

```bash
cd Week-04-Expense-Tracker
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows Command Prompt
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Running the application

```bash
python -m expense_tracker.main add --description "Lunch" --amount 150 --category "Food"
python -m expense_tracker.main add --description "Bus fare" --amount 40 --category "Travel"
python -m expense_tracker.main list
python -m expense_tracker.main total
python -m expense_tracker.main delete --id 1
python -m expense_tracker.main list
```

The first two commands create records, `list` displays them, `total` displays their combined amount, and `delete` removes the requested ID. Add `--date YYYY-MM-DD` to provide a date explicitly.

## Testing

Run `pytest -v`. The tests cover adding, listing-related data, totals, deletion (including missing IDs), invalid amounts, empty lists, JSON persistence, and corrupted JSON handling. Tests use temporary paths and do not modify application data.

## Expected output

Example output after adding the first record:

```text
Added expense 1: Lunch (150.00)
```

Listing and totaling can look like:

```text
ID   Description                Amount Category        Date
1    Lunch                      150.00 Food            2026-11-09
2    Bus fare                    40.00 Travel          2026-11-09
Total expenses: 190.00
```

Deleting ID 1 prints `Deleted expense 1.`. A successful test run ends with output similar to `7 passed`.

## Troubleshooting

- If `python` is not found, install Python 3 and ensure it is on `PATH`; some systems use `python3`.
- If pytest is unavailable, activate `.venv` and run `python -m pip install -r requirements.txt`.
- Amounts must be numeric and greater than zero.
- A missing JSON file is recreated when an expense is added. A corrupted JSON file produces an error; restore valid JSON such as `[]` or remove the file and add an expense again.
