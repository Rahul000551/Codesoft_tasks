todo_list = []

def show_menu():
    print("\n📝 TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:

        for idx, task in enumerate(todo_list, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{idx}. {task['title']} - {status}")

def add_task():
    title = input("Enter new task: ")
    todo_list.append({"title": title, "done": False})
    print("Task added!")

def update_task():
    view_tasks()
    try:
        idx = int(input("Task number to update: ")) - 1
        new_title = input("Enter new title: ")
        todo_list[idx]['title'] = new_title
        print("Task updated.")
    except:
        print("Invalid input.")

def mark_done():
    view_tasks()
    try:
        idx = int(input("Task number to mark as done: ")) - 1
        todo_list[idx]['done'] = True
        print("Task marked as done.")
    except:
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        idx = int(input("Task number to delete: ")) - 1
        del todo_list[idx]
        print("Task deleted.")
    except:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        mark_done()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")