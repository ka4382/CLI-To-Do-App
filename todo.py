tasks = []

def add_tasks(task : str):
    tasks.append(task)
    print("Tasks added.")

def view_tasks():
    for index , task in enumerate (tasks):
        print(f"{index+1}.{task}")

def delete_task(index : int):
    if 0 <= index <= len(tasks):
        tasks.pop(index)
        print("tasks deleted.")
    else:
        print("Invalid Index.")

while True :
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        task = input("Enter Task :")
        add_tasks(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter task number to Delete: ")) - 1
        delete_task(index)
    elif choice == "4":
        break

    else:
        print("Invalid Choice.")