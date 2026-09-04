'''
Project:- 04
Expense Tracker
'''

print("====================")
print(" Expense Tracker")
print("====================")

expenses = []

while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expenese")
    print("4. Exit")

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
        print("Thanks for using Expense Tracker!!")
        break
    else:
        print("Invalid Input!!")
        break

    