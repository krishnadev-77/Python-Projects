"""
Project :- 3
TO-DO-LIST
"""

tasks = []

while True:
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice :")

    if choice == "1":
        work = input("Enter your task :")
        tasks.append(work)
    elif choice == "2":
        for index , task in enumerate(tasks):
            print(index + 1,task)
    elif choice == "3":
        for index, task in enumerate(tasks):
            print(index+1,task)
        task_number = int(input("Enter task number to complete :"))

        tasks[task_number - 1] = tasks[task_number - 1] + "✅"
    elif choice == "4":
        removal = int(input('Enter which task to remove :'))
        tasks.pop(removal -1)
    elif choice == "5":
        print("Thanks for using TO-DO-LIST !!")
        break
    else:
        print("Invalid input!!")
        break

            