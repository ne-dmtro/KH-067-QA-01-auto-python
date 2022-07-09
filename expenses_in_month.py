import csv


def get_month_expenses():
    while True:
        try:
            month = input("Enter the month of expenses: ").lower()
            months = ['january', 'february', 'march', 'april',
                      'may', 'june', 'july', 'august', 'september',
                      'october', 'november', 'december']
            if month in months:
                break
            else:
                raise ValueError("Error: Invalid month.")
        except ValueError:
            print("Error: Invalid month.")

    with open("expenses.csv") as fin:
        if month == 'january':
            total = 0
            for row in csv.reader(fin):
                if '2022-01-01' <= row[0] <= '2022-01-31':
                    total += float(row[2])
            print(f'Your expenses in january = {total}')
        if month == 'february':
            total = 0
            for row in csv.reader(fin):
                if '2022-02-01' <= row[0] <= '2022-01-28':
                    total += float(row[2])
            print(f'Your expenses in february = {total}')
        if month == 'march':
            total = 0
            for row in csv.reader(fin):
                if '2022-03-01' <= row[0] <= '2022-03-31':
                    total += float(row[2])
            print(f'Your expenses in march = {total}')
        if month == 'april':
            total = 0
            for row in csv.reader(fin):
                if '2022-04-01' <= row[0] <= '2022-04-30':
                    total += float(row[2])
            print(f'Your expenses in april = {total}')
        if month == 'may':
            total = 0
            for row in csv.reader(fin):
                if '2022-05-01' <= row[0] <= '2022-05-31':
                    total += float(row[2])
            print(f'Your expenses in may = {total}')
        if month == 'june':
            total = 0
            for row in csv.reader(fin):
                if '2022-06-01' <= row[0] <= '2022-06-30':
                    total += float(row[2])
            print(f'Your expenses in june = {total}')

        elif month == 'july':
            total = 0
            for row in csv.reader(fin):
                if '2022-07-01' <= row[0] <= '2022-07-31':
                    total += float(row[2])
            print(f'Your expenses in july = {total}')
        if month == 'august':
            total = 0
            for row in csv.reader(fin):
                if '2022-08-01' <= row[0] <= '2022-08-31':
                    total += float(row[2])
            print(f'Your expenses in august = {total}')
        if month == 'september':
            total = 0
            for row in csv.reader(fin):
                if '2022-09-01' <= row[0] <= '2022-91-30':
                    total += float(row[2])
            print(f'Your expenses in september = {total}')
        if month == 'october':
            total = 0
            for row in csv.reader(fin):
                if '2022-10-01' <= row[0] <= '2022-10-31':
                    total += float(row[2])
            print(f'Your expenses in october = {total}')
        if month == 'november':
            total = 0
            for row in csv.reader(fin):
                if '2022-11-01' <= row[0] <= '2022-11-30':
                    total += float(row[2])
            print(f'Your expenses in november = {total}')
        if month == 'december':
            total = 0
            for row in csv.reader(fin):
                if '2022-12-01' <= row[0] <= '2022-12-31':
                    total += float(row[2])
            print(f'Your expenses in december = {total}')


get_month_expenses()