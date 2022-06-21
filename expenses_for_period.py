import csv
import date_input_exceptions


def get_expenses_for_period():
    first_date = input("Enter the first date in format 'YYYY-MM-DD': ")
    date_input_exceptions.check_input(first_date)
    second_date = input("Enter the second date in format 'YYYY-MM-DD': ")
    date_input_exceptions.check_input(second_date)
    with open("expenses.csv") as fin:
        total = 0
        for row in csv.reader(fin):
            if first_date <= row[0] <= second_date:
                total += float(row[2])
        print(f'Your expenses for this period = {total}')
