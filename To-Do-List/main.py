'''
to do list
'''

def menu():
    print('''========== TO-DO LIST ==========
    1. View Tasks
    2. Add Task
    3. Mark Task as Completed
    4. Delete Task
    5. Clear all task
    6. Exit''')
    
def viewTask():
    tasks = loadTask()
    if not tasks:
        print("No tasks available.")
        return True
    count = 1
    for task in tasks:
        print(f"{count}. {task}", end="")
        count += 1
    return True
    
def addTask():
    tasks = loadTask()
    r = int(input("How many tasks you want to add?  "))
    for i in range(r):
        x = input()
        tasks.append("[  ] " + x + "\n")
    saveTask(tasks)
    print("Task added successfully")
            
def markTask():
    tasks = loadTask()
    task = int(input("Enter task number: "))
    if 1 <= task <= len(tasks):
        if "[✓]" in tasks[task - 1]:
            print("Task is already marked as completed.")
        else:
            tasks[task - 1] = tasks[task - 1].replace("[  ] ", "[✓] ")
            saveTask(tasks)
            print("Task marked as completed.")
    else:
        print("Invalid task number")
    
def deleteTask():
    tasks = loadTask()
    task = int(input("Enter task number: "))
    if 1 <= task <= len(tasks):
        del tasks[task - 1]
        saveTask(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number")

def clearTask():
    saveTask([])
    print("All tasks cleared.")
        
def loadTask():
    try:
        with open("to-do-list.txt", "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
        
def saveTask(tasks):
    with open("to-do-list.txt", "w") as f:
        f.writelines(tasks)
        
def body():
    try:
        a = int(input("what do you want to do?  "))
        if a == 1:
            viewTask()
            return True
        elif a == 2:
            addTask()
            return True
        elif a == 3:
            markTask()
            return True
        elif a == 4:
            deleteTask()
            return True
        elif a == 5:
            clearTask()
            return True
        elif a == 6:
            print("Thank you for using To-Do List.")
            print("quitting...")
            return False
        else:
            print("Choose between 1 and 6")
            return True
    except ValueError:
        print("Choose between the given choice")
        return True
    
def main():
    while True:
        menu()
        if not body():
            break
    
if __name__ == '__main__':
    main()