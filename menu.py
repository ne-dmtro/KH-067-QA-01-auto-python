import csv


def main_menu():
    print("_____________________")
    print("Main menu options: ")
    print("0 Exit")
    print("1 Income")
    print("2 Expenses")
    print("3 Update")
    print("4 Delete")
    print("_____________________")
def income_menu():
    print("____Income menu____")
    print("0 Exit to main menu")
    print("1 Add Income")
    print("2 Balance")
    print("3 Delete Income")
def expenses_menu():
    pass
def update():
    pass
def delete():
    pass

def add_income():
    date = input("Enter the date in the format....>>")
    income = input("Enter new income >>")
    with open('add_income.csv','w+', newline='') as file:
        writer = csv.writer(file, delimiter="|")
        writer.writerow(['date','income'])
        writer.writerow([date, income])









def balance():
    with open('add_income.csv', 'r') as d:
        reader = csv.reader(d)
        for line in reader:
            print("Your Total income\n", line)


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
                balance()
            elif income_option == "3":
                print("Delete")
            else:
                print("Enter correct number")
    elif option == "2":
        print("____Expenses menu____")
    elif option == "3":
        print ("____Update____")
    elif option == "4":
        print("____Delete____")
    else:
        print("Enter correct number")







