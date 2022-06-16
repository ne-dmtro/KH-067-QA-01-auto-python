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
    #добавляем дату и доход в правильном формате
    # to do - подумать над обработкой исключений
    date = input("Enter date in correct format >>")
    income = input("Enter your Income >>")

    with open('test01.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow([date, income])


def show_income():
    # показывает все доходы по датам
    df = pd.read_csv('test01.csv')
    print(df)

def delete_income():
    #to do  - удаление дохода по интексу
    # del_index = input("Enter index to delete >>")
    # if del_index == index:
    # income_df.drop([1], axis=0)
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







