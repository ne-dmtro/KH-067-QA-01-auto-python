import csv
import re


def get_expenses_for_period():
    while True:
        try:
            first_date = input("Enter the first date in format 'YYYY-MM-DD': ")
            if re.match(r'(\d{4}-\d{2}-\d{2})', first_date):
                break
            else:
                print("Error: Date format invalid.")
        except ValueError:
            print("Error: Date format invalid.")

    while True:
        try:
            second_date = input("Enter the second date in format 'YYYY-MM-DD': ")
            if re.match(r'(\d{4}-\d{2}-\d{2})', second_date):
                break
            else:
                print("Error: Date format invalid.")
        except ValueError:
            print("Error: Date format invalid.")

    with open("expenses.csv") as fin:
        total = 0
        for row in csv.reader(fin):
            if first_date <= row[0] <= second_date:
                total += float(row[2])
        print(f'Your expenses for this period = {total}')


get_expenses_for_period()
