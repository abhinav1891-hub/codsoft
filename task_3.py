
# Contact book-------

contacts = []

def show_menu():
    print("\n=== CONTACT BOOK MENU ===")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found!")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    view_contacts()
    if contacts:
        try:
            contact_no = int(input("Enter contact number to update: "))
            if 1 <= contact_no <= len(contacts):
                contact = contacts[contact_no - 1]
                print("\nLeave field empty to keep current value.")
                name = input(f"Enter new name ({contact['name']}): ") or contact['name']
                phone = input(f"Enter new phone ({contact['phone']}): ") or contact['phone']
                email = input(f"Enter new email ({contact['email']}): ") or contact['email']
                address = input(f"Enter new address ({contact['address']}): ") or contact['address']
                contacts[contact_no - 1] = {"name": name, "phone": phone, "email": email, "address": address}
                print("Contact updated successfully!")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_contact():
    view_contacts()
    if contacts:
        try:
            contact_no = int(input("Enter contact number to delete: "))
            if 1 <= contact_no <= len(contacts):
                removed = contacts.pop(contact_no - 1)
                print(f"Contact '{removed['name']}' deleted successfully!")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Please enter a valid number!")

# Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

