import argparse
from pathlib import Path

from .operations import add_expense, delete_expense, total_expenses
from .storage import StorageError, load_expenses, save_expenses

DATA_FILE = Path(__file__).parent / "data" / "expenses.json"


def build_parser():
    parser = argparse.ArgumentParser(description="Manage personal expenses.")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="add an expense")
    add.add_argument("--description", required=True)
    add.add_argument("--amount", required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--date")
    commands.add_parser("list", help="list expenses")
    commands.add_parser("total", help="calculate total")
    remove = commands.add_parser("delete", help="delete an expense")
    remove.add_argument("--id", required=True, type=int)
    return parser


def run(args, data_file=DATA_FILE):
    expenses = load_expenses(data_file)
    if args.command == "add":
        expense = add_expense(expenses, args.description, args.amount, args.category, args.date)
        save_expenses(data_file, expenses)
        print(f"Added expense {expense['id']}: {expense['description']} ({expense['amount']:.2f})")
    elif args.command == "list":
        if not expenses:
            print("No expenses found.")
            return
        print(f"{'ID':<4} {'Description':<20} {'Amount':>10} {'Category':<15} Date")
        for expense in expenses:
            print(f"{expense['id']:<4} {expense['description']:<20} {expense['amount']:>10.2f} {expense['category']:<15} {expense['date']}")
    elif args.command == "total":
        print(f"Total expenses: {total_expenses(expenses):.2f}")
    elif args.command == "delete":
        deleted = delete_expense(expenses, args.id)
        if deleted is None:
            print(f"Expense {args.id} not found.")
        else:
            save_expenses(data_file, expenses)
            print(f"Deleted expense {args.id}.")


def main():
    parser = build_parser()
    try:
        run(parser.parse_args())
    except (ValueError, StorageError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
