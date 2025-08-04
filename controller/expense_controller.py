from utils.file_manager import (
    read_expenses, write_expense,
    delete_expense, filter_by_category, get_category_totals
)

CSV_PATH = 'expenses.csv'

def add_expense(form):
    date = form['date']
    amount = form['amount']
    category = form['category']
    note = form['note']
    write_expense(CSV_PATH, [date, amount, category, note])

def get_expenses():
    return read_expenses(CSV_PATH)

def remove_expense(index):
    delete_expense(CSV_PATH, index)

def filter_expenses_by_category(category):
    return filter_by_category(CSV_PATH, category)

def get_totals_by_category():
    return get_category_totals(CSV_PATH)

def get_total_spent():
    expenses = read_expenses(CSV_PATH)
    return sum(float(exp[1]) for exp in expenses)

