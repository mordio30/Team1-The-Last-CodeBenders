# Make a program to add, delete, update and read tasks
tasks = [{'taskname': 'moam', 'taskuser': 'me', 'taskdeadline': 'monday', 'prioritylevel': 'low'}

]
priority_level =['high', 'medium', 'low']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def view_tasks():
    for task in tasks:
        print(f"Task: {task['taskname']}")
        print(f"Task Responsibility: {task['taskuser']}")
        print(f"Task Deadline: {task['taskdeadline']}")
        print(f"Task Priority: {task['prioritylevel']}")

def add_task():
    task = {
        'taskname': input("Enter the task name: ").lower(), # Must be a string
        'taskuser': input("Who is responsible for this task: "), # Must be a string
        'taskdeadline': "", # Must be a day & converted to all lowercase
        'prioritylevel': "", # Must be a defined priority & converted to all lowercase
    }
    while True:
        deadline = input("Please choose a day of the week for the task to be completed by: ").lower()
        if deadline in days:
            task['taskdeadline'] = deadline
            break
        else: 
            print("Invalid input. please put a day of the week.")
    while True:
        priority = input("Please choose a priority level of High, Medium, or Low: ").lower()
        if priority in priority_level:
            task['prioritylevel'] = priority
            break
        else: 
            print("Invalid input. Please put a priority level of High, Medium, or Low.")
    tasks.append(task)
    print(f"{ task['taskname'] } successfully added to tasks!")

def delete_task():
    task_to_delete = input("Which task do you want to delete?: ").lower() # The task the user wants to delete
    # iterates through the tasks list of dicts
    for task in tasks:         
        if task['taskname'] == task_to_delete:
            tasks.remove(task)
            print(f"{ task_to_delete } successfully removed from your tasks!")
        # This could be put above the loop so that it checks if the task doesn't exist, it doesn't have to do the loop, so it would save time
        else: print(f" { task_to_delete } does not exist in tasks ")

def update_task():
    task_to_update = input("Which task do you want to update?: ").lower()
    for task in tasks:
        if task['taskname'] == task_to_update:
            # ask what they want to update
            print("Here are your options to update: Task Name, Task Responsibility, Task Deadline, Task Priority.") # maybe put a list of the task items for them to choose from
            item_to_update = input("What do you want to update?: ").lower()
            if item_to_update == 'task name':
                task_name_update = input("What do you want to rename this task to?: ")
                task['taskname'] = task_name_update
                print(f"{ item_to_update } successfully updated!")
            elif item_to_update == 'task responsibility':
                task_responsibility_update = input("Who do you want to reassign this task to?: ").lower()
                task['taskuser'] = task_responsibility_update
                print(f"{ item_to_update } successfully updated!")
            elif item_to_update == 'task deadline':
                task_deadline_update = input("What do you want to change the deadline to?: ")
                task['taskdeadline'] = task_deadline_update
                print(f"{ item_to_update } successfully updated!")
            elif item_to_update == 'task priority':
                task_priority_update = input("What priority level do you want to change this task to?: ")
                task['prioritylevel'] = task_priority_update    
                print(f"{ item_to_update } successfully updated!")
            # 
        else: print(f" { task_to_update } does not exist in tasks ")
            

#add_task()
#add_task()
#print(tasks)
#view_tasks()
#delete_task()
#update_task()
#view_tasks()