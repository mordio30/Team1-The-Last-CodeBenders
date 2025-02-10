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

print(f" {addContact()}")
print(f" {showContacts()}")

#contact search

def contactSearch():
    print(f"{contacts}")
    search = input("enter the contacts name: ")
    if search in contacts:
        print(f"{search}")
    else:
        print(f"No contact was found with that information")

