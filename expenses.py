import pandas as pd

def add_expenses():
    global total_expenses
    expenses = int(input("ввести общее число расходов (например, сколько позиций за день)>> "))
    Date = []
    Name = []
    Expense = []
    for i in range(expenses):
        enter_date = input("дата >>")
        name_of_exp = (input(" описание >>"))
        enter_expense = int(input(" потраченная сумма >>"))
        Date.append(enter_date)
        Name.append(name_of_exp)
        Expense.append(enter_expense)
    dict = {'Expenses Date': Date, 'Name of Expense': Name, 'Your Expenses': Expense}
    df = pd.DataFrame(dict)
    print(df)
    df.to_csv('expenses.csv', mode='a', header=False, index=True)
    total_expenses = df['Your Expenses'].sum()
    print("Общая сумма расходов>>", total_expenses)

add_expenses()
