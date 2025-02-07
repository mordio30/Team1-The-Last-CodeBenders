photos = {}
# family, school, work, pets
    # mom, dad, son, daughter
    # students, teachers
    # boss, coworkers, opsfloor
    # cat, dog, fish, hamster

# display user choices
# ask for inputs for each category
# put everything in while loop to execute code


def view_all_photos():
    print(photos)
    return photos


def add_photo_category():
    category = input("Please Add Photo Category: ")
    photos[category] = []
    print(photos)
    return photos


def view_photo_category():
    category = input("Enter Photo Category to View: ")
    if category in photos:
        print(photos[category])
        return photos
    else:
        print("photo category doesn't exist to view")
        return photos


def delete_photo_category():
    category = input("Enter Photo Category to Delete: ")
    if category in photos:
        del photos[category]
        print(photos)
        return photos
    else:
        print("photo category doesn't exist for deletion")
        return photos
    

# def add_photo_to_category(photo: str):
#     pass


# def add_photo_from_category(photo : str):
#     pass

view_all_photos()
add_photo_category()
add_photo_category()
add_photo_category()
view_photo_category()
view_photo_category()
delete_photo_category()
delete_photo_category()







