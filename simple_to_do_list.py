tasks = []

message = """
What do you want to do?
- To add a task:      'add'
- To remove a task:   'remove'
- To list tasks:      'list'
- To quit:            'quit'
"""

def add(todo):
    return tasks.append(todo)

def remove(todo):
    if todo in tasks:
        return tasks.remove(todo)
    else:
        print("Task not found!")

while True:
    print(message)
    user_input = input("Choice: ").lower()

    if user_input == "add":
        add_todo = input("Enter task to add: ")
        add(add_todo)

    elif user_input == "remove":
        print("Current tasks:", tasks)
        del_todo = input("Enter task to remove: ")
        remove(del_todo)

    elif user_input == "list":
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    elif user_input == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
