import csv


def get_expenses_for_period():
    first_date = input("Enter the first date in format 'YYYY-MM-DD': ")
    second_date = input("Enter the second date in format 'YYYY-MM-DD': ")

    with open("expenses.csv") as fin:
        total = 0
        for row in csv.reader(fin):
            if first_date <= row[0] <= second_date:
                total += float(row[2])
        print(f'Your expenses for this period = {total}')


get_expenses_for_period()
