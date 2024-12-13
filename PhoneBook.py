#Phone Book
#================
def display_menu():
    print("\n Phone Book Menu")
    print("1. Add a contact")
    print("2. Search a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. List all contacts")
    print("6. Exit")
    
def add_contact(phonebook):
    name = input("Enter the contact name : ")
    if(name in phonebook):
        print(f"Name is already exists!! in your phonebook with number{phonebook[name]}")
    else:
        phone = input("Enter phone number ")
        phonebook[name] = phone
        print(f"Contact {name} added successfully")
        

def search_contact(phonebook):
    name = input("Enter the name to be searched in phonebook is ")
    if name in phonebook:
        print(f"The name of the searched contact is {name} and their phone no: {phonebook[name]}")
    else:
        print(f"Contact {name} not found in phonebook")
    
        
def update_contact(phonebook):
    name = input("Enter the name to be updated in the phonebook: ")
    if name in phonebook:
        phonebook[name] = input("Enter the new number to be updated: ")
        print(f"Contact {name} updated successfully")
    else:
        print("There is no such contact exits in phonebook")
        

def delete_contact(phonebook):
    name = input("Enter the contact name to be deleted: ")
    if name in phonebook:
        del phonebook[name]
        print("Deleted Contact")
    else:
        print("No Such Contact Exits")
        
        
def display_contact(phonebook):
    if not phonebook:
        print("No contacts in phonebook")
    else:
        print("\n Phonebook Contact:")
        for name, phone in phonebook.items():
            print(f"Name: {name} Phone: {phone}")   
    
def main():
    phonebook = {}
    while(True):
        display_menu()
        choice = input("Enter Your Choice ")
        
        if choice == "1":
            add_contact(phonebook)
            
        elif choice == "2":
            search_contact(phonebook)
            
        elif choice == "3":
            update_contact(phonebook)
            
        elif choice == "4":
            delete_contact(phonebook)
            
        elif choice == "5":
            display_contact(phonebook)
            
        elif choice == "6":
            print("Exiting the phonebook")
            break
            

main()