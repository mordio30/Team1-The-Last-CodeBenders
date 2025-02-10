# Make a program to add, delete, update and read tasks
tasks = []
priority_level =['high', 'medium', 'low']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def view_tasks():
    print(tasks)

def add_task():
    task = {
        'taskname': input("Enter the task name: ").lower(), # Must be a string
        'taskuser': input("Who is responsible for this task:"), # Must be a string
        'taskdeadline': input("What day should the task be finished by: ").lower(), # Must be a day & converted to all lowercase
        'prioritylevel': input("Please select High, Medium, or Low priority: ").lower(), # Must be a defined priority & converted to all lowercase
    }
    tasks.append(task)

# def delete_task():

add_task()
view_tasks()