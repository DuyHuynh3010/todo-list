from storage import load_tasks, save_tasks

class TodoApp:
    def __init__(self):
        self.tasks = load_tasks()

    def show_tasks(self):
        if not self.tasks:
            print("Your task list is empty.")
            return
        for i, task in enumerate(self.tasks):
            status = "✅" if task['done'] else "❌"
            print(f"{i + 1}. [{status}] {task['task']}")

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        save_tasks(self.tasks)
        print("Task added successfully.")

    def remove_task(self, index):
        try:
            removed = self.tasks.pop(index)
            save_tasks(self.tasks)
            print(f"Removed task: {removed['task']}")
        except IndexError:
            print("Invalid task number!")

    def mark_done(self, index):
        try:
            self.tasks[index]['done'] = True
            save_tasks(self.tasks)
            print("Task marked as done.")
        except IndexError:
            print("Invalid task number!")