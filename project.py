import os
import csv

# Using a global dictionary
contacts = {
    "john": {
        "phone": "6381794609",
        "email": "guruviswa2006@gmail.com"
    },
    "Alice": {
        "phone": "9626546419",
        "email": "gvmarvel@gmail.com"
    }
}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact Added!")

def view_contacts():
    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Found: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        contacts[name]["phone"] = input("New Phone: ")
        contacts[name]["email"] = input("New Email: ")
        print("Updated!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Deleted!")
    else:
        print("Contact not found.")

def save_contacts():
    with open("contacts.txt", "w") as f:
        for name, d in contacts.items():
            f.write(f"{name},{d['phone']},{d['email']}\n")
    print("Contacts saved to contacts.txt")

def load_contacts():
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, phone, email = parts
                    contacts[name] = {"phone": phone, "email": email}

def export_csv():
    with open("contacts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
        for name, d in contacts.items():
            writer.writerow([name, d["phone"], d["email"]])
    print("Exported to contacts.csv")

# Main Loop
load_contacts()
while True:
    print("\n======= CONTACT BOOK ========")
    print("1.Add 2.View 3.Search")
    print("4.Update 5.Delete 6.Save")
    print("7.Export CSV  8.Exit")
    choice = input("Your choice: ")
    
    if choice == "1": add_contact()
    elif choice == "2": view_contacts()
    elif choice == "3": search_contact()
    elif choice == "4": update_contact()
    elif choice == "5": delete_contact()
    elif choice == "6": save_contacts()
    elif choice == "7": export_csv()
    elif choice == "8":
        save_contacts()
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")