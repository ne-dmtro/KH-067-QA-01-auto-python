import pandas as pd

def add_income():
    global total_incomes
    Date = []
    Income = []
    enter_date = input("Enter the date >>")
    enter_income = int(input("Enter your Income >>"))
    Date.append(enter_date)
    Income.append(enter_income)
    dict = {'Income Date': Date, 'Your Income': Income}
    df = pd.DataFrame(dict)
    print(df)
    df.to_csv('incomes.csv', mode='a', header=False, index=True)
    total_incomes = df['Your Income'].sum()
    print("Total>>", total_incomes)


add_income()





