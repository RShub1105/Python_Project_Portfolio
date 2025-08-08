import sqlite3
def create_table():
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,phone TEXT NOT NULL,email TEXT)")
    conn.commit()
    conn.close()

def add_contact(name,phone,email):
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute("INSERT INTO contact(name,phone,email) VALUES (?,?,?)",(name,phone,email))
    conn.commit()
    conn.close()

def view_contact():
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contact")
    for row in c.fetchall():
        print(row)
    conn.close()

def search_contact(name):
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contact WHERE name LIKE ?",('%'+ name + '%',))
    rows = c.fetchall()
    conn.close()
    return rows

def update_contact(name,phone,email,contact_id):
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute("UPDATE contact SET name =?,phone=?,email=? WHERE id=?",(name,phone,email,contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute("DELETE FROM contact WHERE id=?",(contact_id,))
    conn.commit()
    conn.close()

create_table()
while True:
    print("\nContact Manager Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter choice:")
    if choice == "1":
        name = input("NAME : ")
        phone = int(input("Phone no : "))
        email = input("Email.id : ")
        add_contact(name,phone,email)
        print("Contact added")
    elif choice == "2":
        view_contact()
    elif choice == "3":
        keyword = input("Enter The Name To Search : ")
        result = search_contact(keyword)
        for contact in result:
            print(contact)
    elif choice == "4":
        id = int(input("Enter Id of contact to update :  "))
        name = input("New Name : ")
        phone = int(input(" New Phone : "))
        email = input("New Email.Id : ")
        update_contact(id, name, phone , email)
        print("Contact Updated")
    elif choice == "5":
        id = int(input("Enter Id of the contact to Delete:"))
        delete_contact(id)
        print("Contact Deleted")
    elif choice == "6":
        print("Exiting Contact Manager👋🏻")
        break
    else:
        print("invalid choice!")
