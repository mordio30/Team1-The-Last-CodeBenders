#show all contacts when contacts are opened
contacts = []


def showContacts():
    if contacts:
        print("Contacts List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Number: {contact['number']}")
    else:
        print("No contacts available.")

showContacts()

#add contacts
def addContact():
    firstName =(input("Enter new contacts first name: "))
    lastName = (input("Enter new contacts last name: "))
    fullName = firstName + ' ' + lastName
    contactNumber = (input("Enter new contact number: "))
    contactEmail = (input("Enter new contacts email: "))
    newContact = {'name': fullName, 'number' : contactNumber, 'email' : contactEmail}

    contacts.append(newContact)
    # print(f"you have added {newContact} to your Contacts")
    

    return f"you have added {newContact} to your Contacts"

#print(f" {addContact()}")
#print(f" {showContacts()}")

#contact search

def contactSearch():
    print(f"{contacts}")
    search = input("enter the contacts name you would like to search for: ").lower()
    found_contact = []

    for contact in contacts: 
        if search in contact['name'].lower():
            found_contact.append(contact)
    if found_contact:
        print(f"Contact(s) found from search:")
        #print(f"Name: {found_contact['name']}, Number: {found_contact['number']}, Email: {found_contact['email']}")
        for i, contact in enumerate(found_contact):
            print(f"{i+1}: Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}")     

    else:
        print(f"No contact was found with that search information")


#contactSearch()        
showContacts()

def contactDelete():
    global contacts
    search = input("enter the contacts name you want to be deleted: ").lower()
    toDelete = None
    duplicate_contacts = []
    print(contacts)
   
        
    for contact in contacts: 
        if search in contact['name'].lower():
            duplicate_contacts.append(contact)
    if not duplicate_contacts:
        noDupes = "There are no duplicate contacts"
        return noDupes
    if len(duplicate_contacts) > 1:
        print(f"Multiple contacts found:")
        for i, contact in enumerate(duplicate_contacts):
            print(f"{i+1}: Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}")
        try: 
            choice= int(input("Enter the number of the contact you want to delete: "))
            if choice < 0 or choice >= len(duplicate_contacts):
                print("Nothing was deleted due to invalid input")
                return
            toDelete = duplicate_contacts[choice]
        except ValueError:
            print("Invalid input, Please enter a number.")
            return
    else:
        toDelete = duplicate_contacts[0]
    contacts.remove(toDelete)
    return f"Contact deleted: {toDelete['name']} ({toDelete['number']})"

                    


print(addContact())
print(addContact())
print(showContacts())
print(addContact())
print(contactDelete()) 
print(contactSearch())        
print(showContacts())
