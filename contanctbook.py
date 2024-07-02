
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, search_term):
        for contact in self.contacts:
            if contact.name == search_term or contact.phone == search_term:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                return
        print("Contact not found.")

    def update_contact(self, search_term, new_name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact.name == search_term or contact.phone == search_term:
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if contact.name == search_term or contact.phone == search_term:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(search_term, new_name, new_phone, new_email, new_address)
        elif choice == '5':
            search_term = input("Enter name or phone number of the contact to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    #Here's a Python program for a contact book that stores names, phone numbers, emails, and addresses. The program allows users to add new contacts, view all contacts, search contacts by name or phone number, update contact details, and delete contacts. The user interface is designed to be user-friendly for easy interaction.

python#