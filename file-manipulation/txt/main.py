from agenda import add_contact, view_contacts, delete_contacts


def main():
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            break
        else:
            print("Please enter a valid option")


if __name__ == "__main__":
    main()
