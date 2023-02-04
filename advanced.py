import tkinter as tk
from tkinter import messagebox
import random

def rock():
    computer = random.choice(["rock", "paper", "scissors"])
    if computer == "rock":
        result = "Tie"
    elif computer == "paper":
        result = "Computer Wins"
        computer_score[0] += 1
    elif computer == "scissors":
        result = "You Win"
        user_score[0] += 1
    messagebox.showinfo("Result", f"Your Choice: Rock\nComputer's Choice: {computer}\n{result}")

def paper():
    computer = random.choice(["rock", "paper", "scissors"])
    if computer == "rock":
        result = "You Win"
        user_score[0] += 1
    elif computer == "paper":
        result = "Tie"
    elif computer == "scissors":
        result = "Computer Wins"
        computer_score[0] += 1
    messagebox.showinfo("Result", f"Your Choice: Paper\nComputer's Choice: {computer}\n{result}")

def scissors():
    computer = random.choice(["rock", "paper", "scissors"])
    if computer == "rock":
        result = "Computer Wins"
        computer_score[0] += 1
    elif computer == "paper":
        result = "You Win"
        user_score[0] += 1
    elif computer == "scissors":
        result = "Tie"
    messagebox.showinfo("Result", f"Your Choice: Scissors\nComputer's Choice: {computer}\n{result}")

def quit_game():
    root.quit()

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

user_score = [0]
computer_score = [0]

rock_icon = tk.PhotoImage(file="images/rock.png")
paper_icon = tk.PhotoImage(file="images/paper.png")
scissors_icon = tk.PhotoImage(file="images/scissors.png")

rock_button = tk.Button(root, image=rock_icon, command=rock)
paper_button = tk.Button(root, image=paper_icon, command=paper)
scissors_button = tk.Button(root, image=scissors_icon, command=scissors)

rock_button.pack(pady=20)
paper_button.pack(pady=20)
scissors_button.pack(pady=20)

score_label = tk.Label(root, text=f"Your Score: {user_score[0]}  Computer's Score: {computer_score[0]}")
score_label.pack(pady=20)

quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack(pady=20)

root.mainloop()
