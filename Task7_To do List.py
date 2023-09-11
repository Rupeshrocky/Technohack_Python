# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view the to-do list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to remove a task from the to-do list
def remove_task(index):
    if 1 <= index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("Options:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        index = int(input("Enter the task number to remove: "))
        remove_task(index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
