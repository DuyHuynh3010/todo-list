from todo import TodoApp

def main():
    app = TodoApp()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as done")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == "1":
            app.show_tasks()
        elif choice == "2":
            task = input("Enter task description: ")
            app.add_task(task)
        elif choice == "3":
            index = int(input("Enter task number to remove: "))
            app.remove_task(index - 1)
        elif choice == "4":
            index = int(input("Enter task number to mark as done: "))
            app.mark_done(index - 1)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()