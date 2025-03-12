# to do list item 1 : complete/incomplete
# Load existing items
# Create a new item
# List items
# Mark item as complete
# Save items

# JSON : JavaScript Object Notation
import json

#{"tasks": [
#    {"task": "task is this", "complete": True}
#]}

file_name = "todo_list.json"

def load_tasks():
    # create file object
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}
    
def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            # dump takes json dictionnary and put it into the file
            json.dump(tasks, file)
    except:
        print("Failed to save")

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("no task to display")
    else:
        print("Your To-Do list: ")
        for idx, task in enumerate(task_list):
                status = "[Completed]" if task["complete"] else "[Pending]"
                # use different quotes inside quotes to separate
                print(f"{idx + 1}.{task['description']} | {status}")

def create_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added")
    else:
        print("Description cannot be empty")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            # minus 1 because in list index 
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete")
        else:
            print("Invalid task number")
    except:
        print("Enter a valid number")

def mark_task_incomplete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as incomplete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            # minus 1 because in list index 
            tasks["tasks"][task_number - 1]["complete"] = False
            save_tasks(tasks)
            print("Task marked as incomplete")
        else:
            print("Invalid task number")
    except:
        print("Enter a valid number")

def delete_tasks(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as incomplete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            # minus 1 because in list index 
            del tasks["tasks"][task_number - 1]
            save_tasks(tasks)
            print("Task deleted")
        else:
            print("Invalid task number")
    except:
        print("Enter a valid number")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Mark Task as incomplete")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            mark_task_incomplete(tasks)
        elif choice == "5":
            delete_tasks(tasks)
        elif choice == "6":
            print("Good Bye")
            break
        else:
            print("Invalid choice. Please try again.")

main()