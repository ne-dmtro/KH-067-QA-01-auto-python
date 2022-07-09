import pandas as pd

def delete_expenses():
    while True:
        try:
            mark = int(input("How many rows of expenses you want to delete? : "))
            break
        except:
            print('Invalid input. Enter an integer number')


    pd.read_csv('expenses.csv', skipfooter=mark, engine='python').to_csv('expenses.csv', index=False)


delete_expenses()