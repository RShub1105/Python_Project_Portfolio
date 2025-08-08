import sqlite3
def create_table():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, age INTEGER)")
    conn.commit()
    conn.close()
def add_student(name,age):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("INSERT INTO students (name,age)VALUES(?,?)",(name,age))
    conn.commit()
    conn.close()
def view_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT*FROM students")
    for row in c.fetchall():
        print(row)
    conn.close()
create_table()
while True:
    print("\n1.Add Students\n2.View Students\n3.Exit")
    choice = input("Enter your choice :")
    if choice == "1":
        name = input("Enter Name : ")
        age = int(input("Enter the Age : "))
        add_student(name,age)
        print("Students added.")
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invaid choice!")
