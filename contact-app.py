import json

contacts = {}

def add_contacts():
    contact_name = input("Enter contact name: ").strip()
    contact_number = input("Enter contact number: ").strip()
    contacts[contact_name] = contact_number


def show_help():
    print(
        """
        'a' - add contact
        'v' - view all contacts
        'd' - delete contact
        's' - search contact
        'q' - quit app
        """
    )


def view_contacts():
    index = 1
    for key in contacts:
        print(
            f"""
{index}. Name : {key}
   Number : {contacts[key]}"""
        )
        index += 1


def delete_contacts():
    search_name = input("What is the name of the contact you looking for? : ").strip().lower()
    found = False
    del_name = ""
    for con_name in contacts:
        if con_name.lower() == search_name:
            del_name = con_name
            found = True
            print(f"Contact {con_name} deleted successfully")
    if not found:
        print("No such contact exist")
        return
    contacts.pop(del_name)


def search_contacts():
    search_name = input("What is the name of the contact you looking for? : ").strip().lower()
    found = False
    for con_name in contacts:
        if con_name.lower() == search_name:
            con_number = contacts[con_name]
            print(
                f"""
    Name: {con_name}
    Number: {con_number}
"""
            )
            found = True
    if not found:
        print("No such contact exist")

def store_contacts():
    with open("save.json", 'w') as f:
        json.dump(contacts, f, indent=4)
    with open("contacts.txt", 'w') as f:
        index = 1
        for key in contacts:
            save_str = f"""{index}. Name : {key}
   Number : {contacts[key]}
"""
            f.write(save_str)
            index += 1

def restore_contacts():
    global contacts
    try:
        with open("save.json", 'r') as f:
            contacts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}

restore_contacts()
print("Type 'h' to view commands")

while True:
    user_inp = input("What do you want to do? (a,v,d,s,q): ").strip()
    if user_inp == "h":
        show_help()
    elif user_inp == "a":
        add_contacts()
    elif user_inp == "v":
        view_contacts()
    elif user_inp == "d":
        delete_contacts()
    elif user_inp == "s":
        search_contacts()
    elif user_inp == "q":
        store_contacts()
        break
    else:
        print("Invalid input")
