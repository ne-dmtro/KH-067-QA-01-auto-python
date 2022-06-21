import csv
import pandas as pd


def main_menu():
    print("_____________________")
    print("Main menu options: ")
    print("0 Exit")
    print("1 Income")
    print("2 Expenses")
    print("_____________________")
def income_menu():
    print("____Income menu____")
    print("0 Exit to main menu")
    print("1 Add Income")
    print("2 Show your Incomes")
    print("3 Delete Income")
def expenses_menu():
    print("0 Exit to main menu")
    print("1 Food Expenses ")
    print("2 Utility bills")
    print("3 Other bills")

def add_income():
    #добавляем индекс, дату и доход в правильном формате
    # to do - подумать над обработкой исключений
    index = input("Enter Income index >>")
    date = input("Enter date in correct format >>")
    income = input("Enter your Income >>")

    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow([index, date, income])


def show_income():
    print("____Income List____")
    # показывает все доходы
    with open('data.csv', "r+") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def delete_income():
    pass

while True:
    main_menu()
    option = input("Please choose an option >>")
    if option == "0":
        break
    elif option == "1":
            income_menu()
            income_option = input("Please choose an option >>")
            if income_option == "0":
                main_menu()
            elif income_option == "1":
                 add_income()

            elif income_option == "2":
                show_income()
            elif income_option == "3":
                show_income()
                delete_income()
                show_income()
            else:
                print("Enter correct number")
    elif option == "2":
        print("____Expenses menu____")
        expenses_menu()
        expenses_option = input("Please choose an option >>")
        if expenses_option == "0":
            main_menu()
        elif expenses_option == "1":
            print("____Food Expenses____")
        elif expenses_option == "2":
            print("____Utility bills____")
        elif expenses_option == "3":
            print("____Other Bills____")
    else:
        print("Enter correct number")







