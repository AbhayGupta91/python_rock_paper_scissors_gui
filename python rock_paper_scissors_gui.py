# task 2
import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    choices = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }
    user_choice_full = choices.get(user_choice.lower())
    if not user_choice_full:
        return "Invalid choice. Please choose Rock, Paper, or Scissors."
    
    if user_choice_full == computer_choice:
        return "Tie"
    elif (
        (user_choice_full == "rock" and computer_choice == "scissors") or
        (user_choice_full == "scissors" and computer_choice == "paper") or
        (user_choice_full == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

def on_play_button_click():
    play_game()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("300x250")
user_choice_var = tk.StringVar()

label_instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors (R/P/S):", font=("Helvetica", 12))
label_instruction.pack(pady=10)

entry_user_choice = tk.Entry(root, textvariable=user_choice_var, font=("Helvetica", 12))
entry_user_choice.pack(pady=10)

button_play = tk.Button(root, text="Play", command=on_play_button_click, font=("Helvetica", 12))
button_play.pack(pady=10)

made_by_label = tk.Label(root, text="Made by: Abhay Gupta", font=("Arial", 10), fg="gray", bg="lightgray")
made_by_label.pack(pady=5)

made_by_label = tk.Label(root, text="Made by: Abhay Gupta", font=("Arial", 10), fg="gray", bg="lightgray")
made_by_label.pack(pady=5)


result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)



root.mainloop()
