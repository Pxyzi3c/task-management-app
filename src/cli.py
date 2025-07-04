from src.core.task import Task
from src.core.task_manager import TaskManager
from datetime import datetime

manager = TaskManager()

def get_input(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("Input cannot be empty.")

def add_task_flow():
    print("\n[ Add New Task ]")
    title = get_input("Title: ")
    description = get_input("Description: ")
    due_date_str = get_input("Due Date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return
    priority = get_input("Priority (Low, Medium, High): ")
    if priority not in ["Low", "Medium", "High"]:
        print("❌ Invalid priority level.")
        return
    status = "Pending"
    task = Task(title, description, due_date, priority, status)
    manager.add_task(task)

def list_tasks_flow():
    print("\n[ All Tasks ]")
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"[{task['id']}] {task['title']} | {task['priority']} | {task['status']} | Due: {task['due_date']}")

def update_task_flow():
    print("\n[ Update Task ]")
    try:
        task_id = int(get_input("Task ID to update: "))
    except ValueError:
        print("❌ Task ID must be an integer.")
        return
    updates = {}
    title = get_input("New Title (leave blank to skip): ", allow_empty=True)
    if title:
        updates["title"] = title
    description = get_input("New Description (leave blank to skip): ", allow_empty=True)
    if description:
        updates["description"] = description
    due_date = get_input("New Due Date (YYYY-MM-DD, leave blank to skip): ", allow_empty=True)
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            updates["due_date"] = due_date
        except ValueError:
            print("❌ Invalid date format.")
    priority = get_input("New Priority (Low/Medium/High, leave blank to skip): ", allow_empty=True)
    if priority:
        if priority in ["Low", "Medium", "High"]:
            updates["priority"] = priority
        else:
            print("❌ Invalid priority level.")
            return
    status = get_input("New Status (Pending/In Progress/Completed, leave blank to skip): ", allow_empty=True)
    if status:
        if status in ["Pending", "In Progress", "Completed"]:
            updates["status"] = status
        else:
            print("❌ Invalid status.")
            return

    if updates:
        manager.update_task(task_id, updates)
    else:
        print("No updates provided.")

def complete_task_flow():
    print("\n[ Complete Task ]")
    try:
        task_id = int(get_input("Task ID to mark complete: "))
        manager.mark_complete(task_id)
    except ValueError:
        print("❌ Task ID must be an integer.")

def delete_task_flow():
    print("\n[ Delete Task ]")
    try:
        task_id = int(get_input("Task ID to delete: "))
        manager.delete_task(task_id)
    except ValueError:
        print("❌ Task ID must be an integer.")

def menu():
    while True:
        print("""
            1. Add Task
            2. List Tasks
            3. Update Task
            4. Mark Task as Complete
            5. Delete Task
            6. Exit
        """)

        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task_flow()
        elif choice == "2":
            list_tasks_flow()
        elif choice == "3":
            update_task_flow()
        elif choice == "4":
            complete_task_flow()
        elif choice == "5":
            delete_task_flow()
        elif choice == "6":
            print("Exiting Task Manager.")
            break
        else:
            print("❌ Invalid choice.")