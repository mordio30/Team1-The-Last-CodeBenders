import manage_tasks
import contacts



# ADD = "add"
# DELETE = "delete"
# UPDATE = "update"

# valid_commands = [
#     ADD, 
#     DELETE,
#     UPDATE,
# ]

# class Command:
#     def __init__(self, key, action):
#         if key not in valid_commands:
#             print("ERROR INVALID COMMAND KEY")
#             return False
        
#         self.key = key
#         self.action = action


# commands = {
#     [ADD]: Command(ADD, manage_tasks.add_task),
#     [DELETE]: Command(DELETE, manage_tasks.delete_task),
#     [UPDATE]: Command(UPDATE, manage_tasks.update_task)
# }

# my_command = commands.get("add")
# print(my_command.key)
# # do the thing
# my_command.action()






def screenTasks_Main():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("****************")
    print("*     Tasks    *")
    print("*      0/0     *")
    print("*              *")  
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *") 
    print("*              *") 
    print("*              *") 
    print("*              *") 
    print("*              *") 
    print("*              *")
    print("****************")
    print()
    print("'add' to ADD tasks")
    print("'back' or 'quit' to LEAVE")
    print()

def screenTasks_Mod(index):
    print()
    print()
    print(f"****************")
    print(f"*     Tasks    *")
    print(f"*      {index+1}/{len(manage_tasks.tasks)}     *")
    print(f"*              *")
    print(f"*  Task Name:  *")
    print(f"     {manage_tasks.tasks[index]['taskname']}      ")
    print(f"*              *") 
    print(f"*    User:     *")
    print(f"      {manage_tasks.tasks[index]['taskuser']}      ")
    print(f"*              *") 
    print(f"*   Deadline:  *")
    print(f"     {manage_tasks.tasks[index]['taskdeadline']}    ") 
    print(f"*              *")
    print(f"*   Priority:  *")
    print(f"     {manage_tasks.tasks[index]['prioritylevel']}    ")
    print(f"****************")
    print()
    print("'add' to ADD tasks")
    print("'delete' to DELETE tasks")
    print("'update' to UPDATE tasks")
    print("'#' of task you want VIEW")
    print("'back' or 'quit' to LEAVE")
    print()

def screenTasks(command = "none"):
    index = 0
    
    if command == "add":
        manage_tasks.add_task()
    elif command == "delete":
        manage_tasks.delete_task()
    elif command == "update":
        manage_tasks.update_task()
    

    try:
        if int(command) > 0:
            if int(command) <= len(manage_tasks.tasks):
                index = int(command) - 1
    except:
        pass
    # elif command == ">":
    #     if (index+1) > (len(manage_tasks.tasks)-1):

    #     pass
    # elif command == "<":
    #     pass

    #index = 0
    if len(manage_tasks.tasks) == 0:
        screenTasks_Main()
    elif len(manage_tasks.tasks) > 0:
        screenTasks_Mod(index)

    



def screenContacts_Main():
    print()
    print()
    print()
    print()
    print()
    print()
    print("****************")
    print("*    Contacts  *")
    print("*      0/0     *")
    print("*              *")  
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *")  
    print("*              *")
    print("*              *")
    print("*              *") 
    print("*              *") 
    print("*              *")
    print("*              *")
    print("****************")
    print()
    print("'add' to ADD Contacts")
    print("'back' or 'quit' to LEAVE")
    print()

def screenContacts_Mod(index):
    print()
    print()
    print("****************")
    print("*    Contacts  *")
    print(f"*    {index+1}/{len(contacts.contacts)}     *")
    print(f"*              *")
    print(f"*    Name:     *")
    print(f"   {contacts.contacts[index]['name']}      ")
    print(f"*              *") 
    print(f"*   Number #:  *")
    print(f"    {contacts.contacts[index]['number']}      ")
    print(f"*              *") 
    print(f"*   Email @:   *")
    print(f"  {contacts.contacts[index]['email']}    ") 
    print(f"*              *")
    print(f"*              *")
    print(f"*              *")
    #print(f"*   Priority:  *")
    #print(f"     {contacts.contacts[index]['prioritylevel']}    ")
    print(f"****************")
    print()
    print("'add' to ADD contacts")
    print("'delete' to DELETE contacts")
    #print("'search' to SEARCH contacts")
    print("'#' of task you want VIEW")
    print("'back' or 'quit' to LEAVE")
    print()

def screenContacts(command = "none"):
    index = 0
    
    if command == "add":
        contacts.addContact()
    elif command == "delete":
        contacts.contactDelete()
    elif command == "search":
        contacts.contactSearch()

    try:
        if int(command) > 0:
            if int(command) <= len(contacts.contacts):
                index = int(command) - 1
    except:
        pass

    if len(contacts.contacts) == 0:
        screenContacts_Main()
    elif len(contacts.contacts) > 0:
        screenContacts_Mod(index)




def screenBrowser():
    print()
    print()
    print()
    print()
    print()
    print()
    print("****************")
    print("*    Browser   *")
    print("*              *")
    print("*              *")  
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *")
    print("*              *")
    print("*              *")
    print("****************")
    print()
    print("'back' or 'quit' to LEAVE")
    print()

def screenPhoto():
    print()
    print()
    print()
    print()
    print()
    print()
    print("****************")
    print("*     Photo    *")
    print("*              *")
    print("*              *")  
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *")
    print("****************")
    print()
    print("'back' or 'quit' to LEAVE")
    print()

def screenMain():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("****************")
    print("*              *")
    print("*    Contacts  *")
    print("*              *")
    print("*    Browser   *")  
    print("*              *")
    print("*     Photo    *") 
    print("*              *")
    print("*     Tasks    *") 
    print("*              *")
    print("*              *")
    print("*              *")
    print("*              *")
    print("*              *")
    print("****************")
    print()
    print("Choose a Distination")
    print("'back' or 'quit' to LEAVE")
    print()


all_my_screen = {
    "main" : screenMain,
    "contacts" : screenContacts,
    "browser" : screenBrowser,
    "photo" : screenPhoto,
    "tasks" : screenTasks,
    
}

screenTasks_commands = {
    "add" : "add",
    "delete" : "delete",
    "update" : "update",
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9'
}
screenContacts_commands = {
    "add" : "add",
    "delete" : "delete",
    "search" : "search",
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9'
}


def listen_for_commands(screen,user):
    if (screen == "tasks") and (user in screenTasks_commands):
        return screenTasks_commands[user]
    elif (screen == "contacts") and (user in screenContacts_commands):
        return screenContacts_commands[user]
    
    else:
        return "none"
        

def quit(input):
    if (input == "quit")  or (input == "back"):   #  if input == "quit"  or "back":
        return False

def phone(call = "main"):
    key = True              # defualt on inifinite loop
    screen = call            # defualt strating value to choose the screen will be "main"
    command = 'none'
    user = "your ma"
    
    while key != False:  
        
        command = listen_for_commands(screen,user)
        if command == "none":
            all_my_screen[screen]() 
        else:
            all_my_screen[screen](command)
        
        #all_my_screen[screen](command)       # my dict where the keys are just names and values are funtions that "show" screen


        user = input()

        
        key = quit(user)   # this line JUST listen for the word "quit" to make the key the false to stop loop
        #phone(user) if user in all_my_screen else ""     #going different screens

        if user in all_my_screen:
            phone(user)

        # listen_for_commands(user)
            

    
    



start = input("type 'start' to turn on your phone ")
phone() if start == "start" else print(), print("sorry no phone for you")
print("phone is off")


