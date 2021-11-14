import sqlite3
import datetime
import openpyxl
d = datetime.datetime.now()
current_date = d.strftime("%Y-%m-%d")

class Expense:
    def __init__(self, amount, categoryID, date):
        self.amount = amount
        self.categoryID = categoryID
        self.date = date
        conn = sqlite3.connect("Expenses.sqlite")
        c = conn.cursor()
        c.execute("INSERT INTO Expense VALUES (NULL ,?,?,?)", (amount, categoryID, date))
        conn.commit()
        conn.close()

def export_to_excel():
    with sqlite3.connect("Expenses.sqlite") as conn:
        script = "SELECT * FROM Expense"
        cursor = conn.cursor()
        cursor.execute(script)
        lists = cursor.fetchall()
        for list in lists:
            print (list)
        print("Export successful!\n")
        conn.commit()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Expenses exported"
    ws.append(["ExpenseID", "Amount", "Category", "Date"])
    for list in lists:
        ws.append(list)
    wb.save(current_date + ".xlsx")
    conn.close()

def adding_expenses():
    with sqlite3.connect("Expenses.sqlite") as conn:
        script = "SELECT * FROM Category"
        cursor = conn.cursor()
        cursor.execute(script)
        items = cursor.fetchall()
        for item in items:
            print(item[0], "-", item[1])
        conn.commit()
    what_category = int(input("To which category does this expense belong? Choose the corresponding number > "))
    what_amount = int(input("What is the amount of the expense? > "))
    Expense(what_amount, what_category, current_date)
    print("Expense successfully added!\n")


def main():
    print("What do you want to do?\n"
          "1 - add expense\n"
          "2 - export expenses to Excel\n"
          "3 - exit")
    order = int(input("> "))
    if order == 3:
        print("Program exited!")

    if order == 1:
        adding_expenses()
        main()

    if order == 2:
        export_to_excel()
        main()

main()
