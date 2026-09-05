'''
Project:- 04
Expense Tracker
'''
import json

print("====================")
print(" Expense Tracker")
print("====================")

expenses = []

while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Save Expense")
    print("6. Load Expense")
    print("7. Exit")

    choice = input("Enter your choice :")

    if choice == "1":
        name1 = input("Enter name of the expense :")
        amnt = float(input("Enter Amount :"))
        Cat = input("Enter the category :")

        expense = {
            "Name": name1,
            "Amount" : amnt,
            "Category" : Cat
        }
        expenses.append(expense)
    elif choice == "2":
        for index , expense in enumerate(expenses):
            print(index + 1,expense)
    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["Amount"]
        print("Total Amount" , total)
    elif choice == "4":
        removal = int(input("Enter the expense you want to Delete :"))
        expenses.pop(removal-1)
    elif choice == "5":
        with open("expenses.json" , "w")as file:
            json.dump(expenses,file)
    elif choice == "6":
        try:
            with open("expenses.json"  , "r")as file:
                expenses = json.load(file)
            print("File Loaded Successfully!!")
        except FileNotFoundError:
            print("No saved expenses found!!")
    elif choice == "7":
        print("Thanks for using Expense Tracker!!")
        break
    else:
        print("Invalid Input!!")
        break

    