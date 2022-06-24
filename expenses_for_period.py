import csv
import re


def get_expenses_for_period():
    correct_first_date = False
    first_date = ''
    while correct_first_date == False:
        first_date = input("Enter the first date in format 'YYYY-MM-DD': ")
        try:
            if re.match(r'(\d{4}-\d{2}-\d{2})', first_date):
                correct_first_date = True
            else:
                raise ValueError("Error: Date format invalid.")
        except ValueError:
            print("Error: Date format invalid.")

    correct_second_date = False
    second_date = ''
    while correct_second_date == False:
        second_date = input("Enter the second date in format 'YYYY-MM-DD': ")
        try:
            if re.match(r'(\d{4}-\d{2}-\d{2})', first_date):
                correct_second_date = True
            else:
                raise ValueError("Error: Date format invalid.")
        except ValueError:
            print("Error: Date format invalid.")

    with open("expenses.csv") as fin:
        total = 0
        for row in csv.reader(fin):
            if first_date <= row[0] <= second_date:
                total += float(row[2])
        print(f'Your expenses for this period = {total}')


get_expenses_for_period()()
