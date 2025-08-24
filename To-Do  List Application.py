"""
Level 2
Task 1 : To-Do List Application
Build a simple command-line-to-do-list application.Users should be able to add, delete, mark as done, and list tasks.
"""

def  show_tasks(tasks):
    if not tasks:
        print('No Tasks available.')
    else:
        print('\n Tasks:')
        for i, task in enumerate(tasks):
            status = 'Done' if task ['completed'] else 'Pending'
            print(f"{i+1}.{task['name']} [{status}]")

def add_task(tasks):
    task_name = input('Enter the task name: ')
    tasks.append({'name': task_name, 'completed':False})
    print('Task added successfully!!')

def mark_completed(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            choice = int(input('Enter task number to mark as completed:'))
            if 1 <= choice  <= len(tasks):
                tasks[choice-1]['completed']  = True
                print('Task marked as completed!')
            else:
                print('Invalid Task Number.')
        except:
            print('Please enter a valid number.')

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            choice = int(input('Enter task number to delete:'))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice-1)
                print(f"Task {removed['name']} deleted!!")
            else:
                print('Invalid Task Number.')
        except:
            print('Please enter a valid number.')

def todo_app():
    tasks = []
    while True:
        print('\n TO-Do List Menu:')
        print('1. Show Tasks')
        print('2. Add Task')
        print('3. Mark Task Completed')
        print('4. Delete Task')
        print('5. Exit')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            mark_completed(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print('Existing program. Goodbye!!')
            break
        else:
            print('Invalid choice, please select from 1 to 5.')

todo_app()