import tkinter as tk
import random

def game():
    choices = ['rock', 'paper', 'scissors']
    user_choice = choice.get()
    computer_choice = random.choice(choices)
    result.config(text="You chose {} and the computer chose {}".format(user_choice, computer_choice))
    if user_choice == computer_choice:
        result.config(text="It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result.config(text="You win!")
        user_wins.set(user_wins.get() + 1)
    else:
        result.config(text="Computer wins!")
        computer_wins.set(computer_wins.get() + 1)

root = tk.Tk()
root.title("Rock, Paper, Scissors")

choice = tk.StringVar()

rock = tk.Radiobutton(root, text="Rock", value="rock", variable=choice)
paper = tk.Radiobutton(root, text="Paper", value="paper", variable=choice)
scissors = tk.Radiobutton(root, text="Scissors", value="scissors", variable=choice)

rock.pack()
paper.pack()
scissors.pack()

play_button = tk.Button(root, text="Play", command=game)
play_button.pack()

result = tk.Label(root)
result.pack()

user_wins = tk.IntVar()
computer_wins = tk.IntVar()

user_wins_label = tk.Label(root, textvariable=user_wins)
user_wins_label.pack()
computer_wins_label = tk.Label(root, textvariable=computer_wins)
computer_wins_label.pack()

root.mainloop()
