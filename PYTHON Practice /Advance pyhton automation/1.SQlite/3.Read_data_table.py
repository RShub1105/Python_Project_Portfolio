import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
row =cursor.fetchall()
for row in row :
    print(row)
conn.close()
