import pandas as pd
from datetime import date

def add_expenses():
    global total_expenses
    expenses = int(input("enter the number of payments >> "))
    Date = []
    Name = []
    Expense = []
    for i in range(expenses):
        name_of_exp = (input(" description of the payment >> "))
        enter_expense = int(input(" amount of money >> "))
        Date.append(date.today())
        Name.append(name_of_exp)
        Expense.append(enter_expense)
    dict = {'Date': Date, 'Name of Expense': Name, 'Your Expense': Expense}
    df = pd.DataFrame(dict)
    print(df)
    df.to_csv('expenses.csv', mode='a+', header=False, index=False)
    total_expenses = df['Your Expense'].sum()
    print("Sum of payments >>", total_expenses)

add_expenses()