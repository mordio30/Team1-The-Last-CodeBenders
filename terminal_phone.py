import manage_tasks

def screenMain():
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

def screenContacts():
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


def screenBrowser():
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


def screenPhoto():
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

def screenTasks():
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
    "main" : screenMain,
    "contacts" : screenContacts,
    "browser" : screenBrowser,
    "photo" : screenPhoto,
    "tasks" : screenTasks,
    
}


def quit(input):
    if (input == "quit")  or (input == "back"):   #  if input == "quit"  or "back":
        return False
    



# def change_Screen(input):
#     if input == "quit":
#         return False
def listen_for_commands(user):
    pass


def phone(call = "main"):
    key = True              # defualt on inifinite loop
    screen = call            # defualt strating value to choose the screen will be "main"
    
    while key != False:  
        all_my_screen[screen]()       # my dict where the keys are just names and values are funtions that "show" screen
        


        user = input()

        listen_for_commands(user)
        key = quit(user)   # this line JUST listen for the word "quit" to make the key the false to stop loop
        phone(user) if user in all_my_screen else ""
            

    
    



start = input("type 'start' to turn on your phone ")
phone() if start == "start" else print("sorry no phone for you")
print("phone is off")


