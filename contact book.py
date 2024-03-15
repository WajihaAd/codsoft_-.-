import re
import time
import os

class Contact:
    def __init__(self, storename, phonenumber, email, address):
        self.storename = storename
        self.phonenumber = phonenumber
        self.email = email
        self.address = address

    def addnew(self):
        os.system("clear")
        print("\033[1;36mAdd new contact: \033[0m")

        time.sleep(2)
        s1 = input("\033[35mEnter your storename: \033[0m")
        while s1.isdigit():
            print("Invalid input")
            s1 = input("\033[35mEnter your storename: \033[0m")

        p1 = input("\033[35mEnter your phonenumber:\033[0m ")
        while len(p1) != 11 or (not p1.startswith("0")):
            print("Invalid phonenumber")
            p1 = input("\033[35mEnter your phonenumber:\033[0m ")
        p1 = int(p1)

        e1 = input("\033[35mEnter your email:\033[0m ")
        if not e1.endswith("@gmail.com"):
            print("Invalid email")
            e1 = input("\033[35mEnter your email:\033[0m ")

        if not self.valid(e1):
            print("Invalid email")
            e1 = input("\033[35mEnter your email: \033[0m")

        print("\033[35mEnter your address:\033[0m ")
        a1 = input("\033[35mCity:\033[0m")
        while a1.isdigit():
            print("Invalid input")
            a1 = input("\033[35mCity:\033[0m")
        b1 = input("\033[35mState:\033[0m")

        with open("contact.txt", "a") as f:
            f.write("--------------------------------------------------------------\n")
            f.write(f"storename: {s1}\nphonenumber: {p1}\nemail: {e1}\naddress: {a1} and {b1}\n")
            f.write("--------------------------------------------------------------\n")

        print("\t\t\t\tPatience is Greatness ", end="", flush=True)
        spinner = ['O', '\\', '|', '/', '-']
        for _ in range(20):
            for char in spinner:
                time.sleep(0.1)
                print('\b' + char, end="", flush=True)
        print('\b', end="")
        print("\r" + " " * len("patience is greatness ") +
              "\rContact added Successfully!!")
        input("Press any key to continue:")

    def valid(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+[^@]@gmail\.com$'
        match = re.match(pattern, email)
        return bool(match)

    def view(self):
        os.system("clear")

        print("\033[1;36mView contact: \033[0m")
        with open("contact.txt", "r") as f:
            print(f.read())
        input("Press any key to continue:")

    def search(self):
        os.system("clear")
        print("\033[1;36mSearch contact: \033[0m")
        found_contacts = []
        search_query = input("Enter the name or phonenumber of the contact you want to search for: ")
        with open("contact.txt", "r") as f:
            contact_block = ""
            for line in f:
                if line.startswith("--------------------------------------------------------------"):
                    if search_query in contact_block:
                        found_contacts.append(contact_block)
                    contact_block = ""
                contact_block += line

            if search_query in contact_block:
                found_contacts.append(contact_block)

        if found_contacts:
            print("Contacts found:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found for the given name or phonenumber.")
        input("Press any key to continue:")

    def delete(self):
        os.system("clear")

        print("\033[1;36mDelete contact: \033[0m")
        search_query = input("Enter the name of the contact you want to delete: ")
        contact_deleted = False

        with open("contact.txt", "r") as f:
            lines = f.readlines()

        with open("contact.txt", "w") as f:
            delete_contact = False
            for line in lines:
                if line.strip() == "--------------------------------------------------------------":
                    delete_contact = False

                if delete_contact:
                    continue

                if f"storename: {search_query}" in line:
                    contact_deleted = True
                    delete_contact = True
                    continue

                f.write(line)

        if contact_deleted:
            print("Contact deleted successfully.")
        else:
            print("No contact found with the given name.")
        input("Press any key to continue:")

    def update(self):
        os.system("clear")

        print("\033[1;36mUpdate contact: \033[0m")
        search_query = input("Enter the name of the contact you want to update: ")
        field_to_update = input("Enter the field you want to update (storename/phonenumber/email/address): ")
        new_value = input(f"Enter the new value for {field_to_update}: ")

        updated = False

        with open("contact.txt", "r") as f:
            lines = f.readlines()

        with open("contact.txt", "w") as f:
            for line in lines:
                if f"storename: {search_query}" in line:
                    updated = True
                    if field_to_update.lower() in line.lower():
                        line = f"{field_to_update}: {new_value}\n"
                f.write(line)

        if updated:
            print("Contact updated successfully.")
        else:
            print("No contact found with the given name.")
        input("Press any key to continue:")


if __name__ == "__main__":
    c = Contact("storename", "phonenumber", "email", "address")
    while True:
        os.system("clear")

        a="\033[1;37mContact Management System\033[0m".center(50)
        print(a)
        print("\033[1;36m1. Add new contact\033[0m")
        print("\033[1;36m2. View contacts\033[0m")
        print("\033[1;36m3. Search contacts\033[0m")
        print("\033[1;36m4. Delete contact\033[0m")
        print("\033[1;36m5. Update contact\033[0m")
        print("\033[1;36m6. Exit\033[0m")
        choice = input("Enter your choice: ")
        if choice == "1":
            c.addnew()
        elif choice == "2":
            c.view()
        elif choice == "3":
            c.search()
        elif choice == "4":
            c.delete()
        elif choice == "5":
            c.update()
        elif choice == "6":
            print("Exiting...")
            time.sleep(2)
            exit()
