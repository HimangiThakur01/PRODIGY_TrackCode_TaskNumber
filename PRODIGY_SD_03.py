class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        print("Contact List:")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def edit_contact(self, index, name, phone, email):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact index.")
            return

        contact = self.contacts[index - 1]
        contact.name = name
        contact.phone = phone
        contact.email = email
        print(f"Contact {name} updated successfully.")

    def delete_contact(self, index):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact index.")
            return

        deleted_contact = self.contacts.pop(index - 1)
        print(f"Contact {deleted_contact.name} deleted successfully.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            index = int(input("Enter the index of the contact to edit: "))
            name = input("Enter New Name: ")
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            contact_manager.edit_contact(index, name, phone, email)
        elif choice == "4":
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index)
        elif choice == "5":
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
