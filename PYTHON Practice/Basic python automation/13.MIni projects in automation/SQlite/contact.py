import sqlite3
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
conn.commit()

def add_contact(name, email):
    try:
        cursor.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"Contact {name} added.")
    except sqlite3.IntegrityError:
        print("Email already exists.")

def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    for row in cursor.fetchall():
        print(row)

def delete_contact(contact_id):
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    print(f"Contact {contact_id} deleted.")
def menu():
    while True:
        print("\nContacts App")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            add_contact(name, email)
            print("Contact Added Succesfullu!")
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

menu()
conn.close()
