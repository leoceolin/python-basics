import os


def add_contact():
    name = input("Enter the contact name: ")
    address = input("Enter the contact address: ")
    email = input("Enter the contact email: ")

    contact = f"Name: {name}, \nAddress: {address}, \nEmail: {email}\n"

    with open("datasets/agenda.txt", "a", encoding="utf-8") as file:
        file.write(contact)

    print("Contact added successfully")


def view_contacts():
    if not os.path.exists("datasets/agenda.txt"):
        print("No contacts found")
        return

    with open("datasets/agenda.txt", "r", encoding="utf-8") as file:
        contacts = file.read()

    print(f"Contacts list: \n{contacts}")


def delete_contacts():
    if not os.path.exists("datasets/agenda.txt"):
        print("No contacts found")
        return

    with open("datasets/agenda.txt", "w", encoding="utf-8") as file:
        file.write("")

    print("Contacts deleted successfully")
