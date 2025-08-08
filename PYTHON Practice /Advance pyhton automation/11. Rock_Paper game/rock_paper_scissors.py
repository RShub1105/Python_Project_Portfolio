import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(player_choice):
    computer_choice = random.choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = "ITS A TIE!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        result = "🏆 YOU WIN!"
    else:
        result = "🖥️🏆 COMPUTER WINS!"

    result_label.config(text=f"You: {player_choice} | Computer: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

for choice in choices:
    tk.Button(button_frame, text=choice, font=("Arial", 12), width=10, command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 14), pady=20)
result_label.pack()

root.mainloop()
