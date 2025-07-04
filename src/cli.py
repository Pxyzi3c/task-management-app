from src.core.task import Task
from src.core.task_manager import TaskManager

manager = TaskManager()

def menu():
    while True:
        print("""
        1. Add Task
        2. List Tasks
        3. Update Task
        4. Mark Complete
        5. Delete Task
        6. Exit
        """)
        choice = input("Choose an option: ")
        if choice == "1":
            pass
        elif choice == "2":
            tasks = manager.list_tasks()
            for t in tasks:
                print(t)
        elif choice == "6":
            break

if __name__ == "__main__":
    menu()