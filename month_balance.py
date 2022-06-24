import csv


def get_month_balance():
    correct_month = False
    month = ''
    while correct_month == False:
        month = input("Enter the month of expenses: ").lower()
        months = ['january', 'february', 'march', 'april',
                  'may', 'june', 'july', 'august', 'september',
                  'october', 'november', 'december']
        try:
            if month in months:
                correct_month = True
            else:
                raise ValueError("Error: Invalid month.")
        except ValueError:
            print("Error: Invalid month.")

    # with open("incomes.csv") as fin:
    #     pass

    month_income = 10000

    with open("expenses.csv") as fin:
        if month == 'january':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-01-01' <= row[0] <= '2022-01-31':
                    month_expenses += float(row[2])
        if month == 'february':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-02-01' <= row[0] <= '2022-01-28':
                    month_expenses += float(row[2])
        if month == 'march':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-03-01' <= row[0] <= '2022-03-31':
                    month_expenses += float(row[2])
        if month == 'april':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-04-01' <= row[0] <= '2022-04-30':
                    month_expenses += float(row[2])
        if month == 'may':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-05-01' <= row[0] <= '2022-05-31':
                    month_expenses += float(row[2])
        if month == 'june':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-06-01' <= row[0] <= '2022-06-30':
                    month_expenses += float(row[2])
        elif month == 'july':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-07-01' <= row[0] <= '2022-07-31':
                    month_expenses += float(row[2])
        if month == 'august':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-08-01' <= row[0] <= '2022-08-31':
                    month_expenses += float(row[2])
        if month == 'september':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-09-01' <= row[0] <= '2022-91-30':
                    month_expenses += float(row[2])
        if month == 'october':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-10-01' <= row[0] <= '2022-10-31':
                    month_expenses += float(row[2])
        if month == 'november':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-11-01' <= row[0] <= '2022-11-30':
                    month_expenses += float(row[2])
        if month == 'december':
            month_expenses = 0
            for row in csv.reader(fin):
                if '2022-12-01' <= row[0] <= '2022-12-31':
                    month_expenses += float(row[2])

    month_balance = month_income - month_expenses
    print(f'Your balance in {month} = {month_balance}')


get_month_balance()
