# Create Terminal Phone Menu Interface
def screnMain():
    print()
    print()
    print("****************")
    print("*    Contacts  *")
    print("*              *")
    print("*    Browser   *")  
    print("*              *")
    print("*     Photo    *") 
    print("*              *")
    print("*     Tasks    *") 
    print("*              *")
    print("****************")

def screnContacts():
    print()
    print()
    print("****************")
    print("*    Contacts  *")
    print("*              *")
    print("*              *")  
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *") 
    print("*              *")
    print("****************")


def screnBrowser():
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
    print("****************")


def screnPhoto():
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
    print("****************")

def screnTasks():
    print()
    print()
    print("****************")
    print("*     Tasks    *")
    print("*              *")
    print("*              *")  
    print("*              *")
    print("*              *") 
    print("*              *")
    print("*              *") 
    print("*              *")
    print("****************")





all_my_screen = {
    "main" : screnMain,
    "contacts" : screnContacts,
    "browser" : screnBrowser,
    "photo" : screnPhoto,
    "tasks" : screnTasks,
    
}


def quit(input):
    if (input == "quit")  or (input == "back"):   #  if input == "quit"  or "back":
        return False
    



# def change_Screen(input):
#     if input == "quit":
#         return False
    


def phone(call = "main"):
    key = True              # defualt on inifinite loop
    screen = call            # defualt strating value to choose the screen will be "main"
    
    while key != False:  
        all_my_screen[screen]()       # my dict where the keys are just names and values are funtions that "show" screen

        user = input()

        key = quit(user)   # this line JUST listen for the word "quit" to make the key the false to stop loop
        phone(user) if user in all_my_screen else ""
            

    
    



start = input("type 'start' to turn on your phone ")
phone() if start == "start" else print("sorry no phone for you")
print("phone is off")



    


# Manage Contacts



# Search on the Internet



# Manage Tasks and Subtasks

