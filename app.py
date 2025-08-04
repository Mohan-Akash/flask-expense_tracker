from flask import Flask, render_template, request, redirect, url_for, session
from controller.expense_controller import (
    add_expense, get_expenses, filter_expenses_by_category,
    get_totals_by_category, remove_expense, get_total_spent
)

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Needed for session handling

@app.route('/')
def index():
    theme = session.get('theme', 'light')
    total_spent = get_total_spent()
    return render_template('index.html', theme=theme, total_spent=total_spent)

@app.route('/toggle-theme')
def toggle_theme():
    current_theme = session.get('theme', 'light')
    session['theme'] = 'dark' if current_theme == 'light' else 'light'
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_expense(request.form)
        return redirect('/view')
    return render_template('add.html')

@app.route('/view')
def view():
    expenses = get_expenses()
    return render_template('view.html', expenses=expenses)

@app.route('/filter', methods=['GET', 'POST'])
def filter_view():
    if request.method == 'POST':
        category = request.form['category']
        filtered = filter_expenses_by_category(category)
        return render_template('view.html', expenses=filtered)
    return render_template('filter.html')

@app.route('/totals')
def totals():
    totals = get_totals_by_category()
    return render_template('totals.html', totals=totals)

@app.route('/remove/<int:index>')
def remove(index):
    remove_expense(index)
    return redirect('/view')

if __name__ == "__main__":
    app.run(debug=True)
