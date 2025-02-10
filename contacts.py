#show all contacts when contatcs are opened
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



#contact search

def contactSearch():
    print(f"{contacts}")
    foundContact = []
    search = input("enter the contacts name: ")
    for contact in contacts:
        if search in contact['name'].lower():
            foundContact.append(contact)
        
    if foundContact:
        print(f"Search result: ")
        for contact in foundContact:
            print(f"name: {contact['name']}, Number: {contact['number']}")
    else:
            print(f"This name : {search} is not in your contacts.")

#print("\n--- Adding a Contact ---")
#print(addContact())

#print("\n--- Showing Contacts ---")
#print(showContacts())

print("\n--- Searching for a Contact ---")
print(contactSearch())