import tkinter as tk
from tkinter import messagebox
import random

options = ['rock', 'paper', 'scissors']

class RockPaperScissors(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Rock Paper Scissors")
        self.geometry("200x200")

        tk.Label(self, text="Your Choice:").pack()

        self.user_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.user_wins = tk.IntVar()
        self.computer_wins = tk.IntVar()
        self.user_wins.set(0)
        self.computer_wins.set(0)

        self.rock_icon = tk.PhotoImage(file="images/rock.png")
        self.paper_icon = tk.PhotoImage(file="images/paper.png")
        self.scissors_icon = tk.PhotoImage(file="images/scissors.png")

        tk.Radiobutton(self, image=self.rock_icon, variable=self.user_choice, value="rock").pack()
        tk.Radiobutton(self, image=self.paper_icon, variable=self.user_choice, value="paper").pack()
        tk.Radiobutton(self, image=self.scissors_icon, variable=self.user_choice, value="scissors").pack()

        tk.Button(self, text="Play", command=self.play).pack()

        tk.Label(self, text="Your Wins:").pack()
        tk.Label(self, textvariable=self.user_wins).pack()

        tk.Label(self, text="Computer Wins:").pack()
        tk.Label(self, textvariable=self.computer_wins).pack()

    def play(self):
        if not self.user_choice.get():
            messagebox.showerror("Error", "Please choose an option")
            return

        self.computer_choice.set(random.choice(options))

        result = self.decide_winner(self.user_choice.get(), self.computer_choice.get())

        if result == "user":
            self.user_wins.set(self.user_wins.get() + 1)
        elif result == "computer":
            self.computer_wins.set(self.computer_wins.get() + 1)
        else:
            messagebox.showinfo("Tie", "It's a tie")

    def decide_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
            return "user"
        else:
            return "computer"

if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop
