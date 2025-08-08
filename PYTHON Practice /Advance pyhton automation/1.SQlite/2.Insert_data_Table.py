import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO students (name, age)VALUES(?,?)",('Rahul',26))
conn.commit()
conn.close()
print("Data Inserted.")