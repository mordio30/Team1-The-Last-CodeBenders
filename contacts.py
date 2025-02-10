#show all contacts when contacts are opened
contacts = []


def showContacts():
    if contacts:
        print("Contacts List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Number: {contact['number']}")
    else:
        print("No contacts available.")

print(f" {showContacts()}")
#add contacts
def addContact():
    firstName =(input("contacts first name: "))
    lastName = (input("contacts last name: "))
    fullName = firstName + ' ' + lastName
    contactNumber = (input("contact number: "))
    contactEmail = (input("contacts email: "))
    newContact = {'name': fullName, 'number' : contactNumber, 'email' : contactEmail}

    contacts.append(newContact)
    

    return newContact

print(f" {addContact()}")
print(f" {showContacts()}")

#contact search

def contactSearch():
    print(f"{contacts}")
    search = input("enter the contacts name: ").lower()
    found_contact = None

    for contact in contacts: 
        if search in contact['name'].lower():
            found_contact = contact
            break
    if found_contact:
        print(f"Contact found :")
        print(f"Name: {found_contact['name']}, Number: {found_contact['number']}, Email: {found_contact['email']}")
                

    else:
        print(f"No contact was found with that information")


contactSearch()        


def contactDelete():
    print(f"{contacts}")
    search = input("enter the contacts name: ").lower()
    toDelete = None

    for contact in contacts: 
        if search in contact['name'].lower():
            toDelete = contact
            break
    if toDelete:
        contacts.remove(toDelete)
        print(f"Contact deleted:")
        print(f"Name: {toDelete['name']}, Number: {toDelete['number']}, Email: {toDelete['email']}")
                

    else:
        print(f"No contact was found with that information")


contactDelete() 
contactSearch()        

