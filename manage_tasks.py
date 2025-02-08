# Make a program to add, delete, update and read tasks
tasks = [

]
priority_level =['high', 'medium', 'low']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def view_tasks():
    print(tasks)

def add_task():
    task = {
        'taskname': input("Enter the task name: ").lower(), # Must be a string
        'taskuser': input("Who is responsible for this task: "), # Must be a string
        'taskdeadline': input("What day should the task be finished by: ").lower(), # Must be a day & converted to all lowercase
        'prioritylevel': input("Please select High, Medium, or Low priority: ").lower(), # Must be a defined priority & converted to all lowercase
    }
    tasks.append(task)

def delete_task():
    task_to_delete = input("Which task do you want to delete?: ").lower() # The task the user wants to delete
    # iterates through the tasks list of dicts
    for task in tasks:
        # print(task)
        # if task_to_delete_value matches i['taskname']           
        if task['taskname'] == task_to_delete:
            tasks.remove(task)
            # new_task_list = (list(filter(lambda)))
            # tasks = new_task_list
        else: print(f" { task_to_delete } does not exist in tasks ")
        
    

       
            


add_task()
add_task()
view_tasks()
delete_task()
view_tasks()
