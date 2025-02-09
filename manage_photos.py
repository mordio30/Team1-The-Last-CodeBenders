boolean = True
choice_list = [1,2,3,4,5,6,7]
photos = {}

def options():
    print("\nEnter 1 to 'View Photo Directory': ")
    print("Enter 2 to 'Add Photo Category': ")
    print("Enter 3 to 'View Photo Category': ")
    print("Enter 4 to 'Delete Photo Category': ")
    print("Enter 5 to 'Add Photo to Category': ")
    print("Enter 6 to 'Delete Photo Fro Category': ")
    print("Enter 7 to 'Exit Photo Category\n")

def view_all_photos():
    print(photos)
    return photos


def add_photo_category():
    category = input("Please Add Photo Category: ").lower()
    photos[category] = []
    print(f"{category} Photo Category Added!\n")
    return photos


def view_photo_category():
    category = input("Enter Photo Category to View: ").lower()
    if category in photos:
        print(photos[category])
        return photos
    else:
        print(f"{category} Photo Category Doesn't Exist to View!\n")
        return photos


def delete_photo_category():
    category = input("Enter Photo Category to Delete: ").lower()
    if category in photos:
        del photos[category]
        print(f"{category} Photo Category Deleted!\n")
        return photos
    else:
        print(f"{category} Photo Category Doesn't Exist for Deletion!\n")
        return photos
    

def add_photo_to_category():
    category = input("Enter Photo Category for Adding Photo: ").lower()
    if category not in photos:
        print(f"{category} Photo Category Doesn't Exist!\n")
        return photos
    photo = input("Add Photo Name: ").lower()
    photos[category].append(photo)
    return photos

def delete_photo_from_category():
    category = input("Enter Photo Category for Deleting Photo: ").lower()
    if category not in photos:
        print(f"{category} Photo Category Doesn't Exist!\n")
        return photos
    photo = input("Enter Photo Name to Delete: ").lower()
    flag = any(x == photo for x in photos[category])
    if not flag:
        print(f"{photo} Photo Doesn't Exist in {category} Category!\n")
        return photos
    photos[category].remove(photo)
    print(f"{photo} Photo Deleted From {category} Category!\n")
    return photos

while boolean == True:
    options()
    try: 
        option = int(input())
        flag = any(x == option for x in choice_list)
        if not flag:
            print("Invalid Number! Try Again!\n")
        if option == 1:
            view_all_photos()
        elif option == 2:
            add_photo_category()
        elif option == 3:
            view_photo_category()
        elif option == 4:
            delete_photo_category()
        elif option == 5:
            add_photo_to_category()
        elif option == 6:
            delete_photo_from_category()
        elif option == 7:
            boolean = False
    except ValueError: 
        print("Invalid Choice! Try Again!\n")
        continue
    
# enter invalid choice: 8
# enter invalid choice: gh
# add_photo_category() # family 
# add_photo_category() # school
# add_photo_category() # work
# add_photo_to_category() # family, porky
# add_photo_to_category() # family, tweety
# add_photo_to_category() # school, bugs
# add_photo_to_category() # work, assessment
# view_photo_category() # family
# view_photo_category() # pets
# delete_photo_category() school
# delete_photo_category() pets
# delete_photo_from_category() # pets
# delete_photo_from_category() # family, oscar
# delete_photo_from_category() # family, porky
# view_all_photos()
# quit()
