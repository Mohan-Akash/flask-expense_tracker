import csv
import os

def ensure_csv_file(path):
    if not os.path.exists(path):
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'amount', 'category', 'note'])

def read_expenses(path):
    ensure_csv_file(path)
    with open(path, 'r') as f:
        return list(csv.reader(f))[1:]

def write_expense(path, row):
    data = read_expenses(path)
    data.append(row)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'amount', 'category', 'note'])
        writer.writerows(data)

def delete_expense(path, index):
    data = read_expenses(path)
    if 0 <= index < len(data):
        data.pop(index)
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'amount', 'category', 'note'])
            writer.writerows(data)

def filter_by_category(path, category):
    data = read_expenses(path)
    return [row for row in data if row[2].lower() == category.lower()]

def get_category_totals(path):
    data = read_expenses(path)
    totals = {}
    for row in data:
        category = row[2]
        amount = float(row[1])
        totals[category] = totals.get(category, 0) + amount
    return [[cat, amt] for cat, amt in totals.items()]
