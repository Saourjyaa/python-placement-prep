from datetime import date


def validate_amount(amount):
    try:
        value = float(amount)
    except (TypeError, ValueError) as error:
        raise ValueError("Amount must be a number.") from error
    if value <= 0:
        raise ValueError("Amount must be greater than zero.")
    return round(value, 2)


def add_expense(expenses, description, amount, category, expense_date=None):
    if not description.strip() or not category.strip():
        raise ValueError("Description and category cannot be empty.")
    next_id = max((int(item["id"]) for item in expenses), default=0) + 1
    expense = {
        "id": next_id,
        "description": description.strip(),
        "amount": validate_amount(amount),
        "category": category.strip(),
        "date": expense_date or date.today().isoformat(),
    }
    expenses.append(expense)
    return expense


def total_expenses(expenses):
    return round(sum(float(item["amount"]) for item in expenses), 2)


def delete_expense(expenses, expense_id):
    for index, expense in enumerate(expenses):
        if int(expense["id"]) == expense_id:
            return expenses.pop(index)
    return None
