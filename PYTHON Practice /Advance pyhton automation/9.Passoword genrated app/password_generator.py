import tkinter as tk
import random
import string

def generator_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters)for _ in range(length))
    password_entry.delete(0,tk.END)
    password_entry.insert(0,password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

tk.Label(root,text="Password length:",font=('Arial',12)).pack(pady=5)

length_entry = tk.Entry(root,font=('Arial',12))
length_entry.pack()

tk.Button(root,text="Generate Password",font=('Arial',12),command=generator_password).pack(pady=10)

password_entry = tk.Entry(root,font=('Arial',12),width=30)
password_entry.pack()

root.mainloop()