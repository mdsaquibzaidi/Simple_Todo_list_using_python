#create the simple python doto list program

to_do= []

#function of add a New Task
def add_task():
    task = input("Enter the task:")
    to_do.append({"Task": task,"Status": "pending"})
    print("New Task Will Added Successfully !!!\n\n")

#function of view all Task
def view_task():
    print("Your TODO List :")
    if len(to_do) == 0:
        print("No Any Pending Task:\n")
    else:
        for index, task in enumerate(to_do,1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")


#function to remove task
def remove_task():
    if len(to_do) == 0:
        print("Your Todo list is Empty...\n\n")
    else:
        try:
            for index, task in enumerate(to_do, 1):
                    print(f"{index}: {task['Task']} - {task['Status']}")
            print("\n")

            search_item = int(input("Enter the Task Number That You Want To Delete:")) -1
            if 0 <= search_item < len(to_do):
                remove_task = to_do.pop(search_item)
                print(f"The Task is Removed :{remove_task['Task']} \n")
        except ValueError:
            print("Please Enter Valid Task Number.\n\n")


#function of for task done
def done_task():
    if len(to_do) == 0:
        print("Your Task List is Empty...\n")
    else:
        try:
            for index, task in enumerate(to_do, 1):
                print(f"{index}: {task['Task']} - {task['Status']}")
            print("\n")

            search_item = int(input("Enter the Task Number That You complete:\n")) - 1
            if 0 <= search_item < len(to_do):
                to_do[search_item]['Status'] = "it's done!!"
                print(f"Task {to_do[search_item]['Task']} has been marked as completed. \n ")
        except ValueError:
            print("Please Enter Valid Task Number.")


#menu bar to show the terminal
def menu():
    while True:
        print("*** menu bar ***")
        print("1. Add a New Task:")
        print("2. View All Tasks:")
        print("3. Remove a Task:")
        print("4.Mark a Task as complete:")
        print("5. Exit ")

        choice=int(input("Enter the choice:"))
        if choice== 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            done_task()
        elif choice == 5:
            print("Thanks for using we will meet again !!!")
            exit()
        else:
            print("Invalid choice please correct one.")
menu()
