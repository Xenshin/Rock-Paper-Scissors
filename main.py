import random

print("Welcome to the Rock, Paper, Scissors game!")

# Game loop
while True:
    # Get user's choice
    user_choice = input("Please enter your choice (rock, paper, or scissors): ")
    user_choice = user_choice.lower()
    # check the input is valid or not
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        continue

    # Get computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer's choice:", computer_choice)

    your_score = 0
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
        print("your total score: ", your_score)
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        your_score += 1
        print("your total score: ", your_score)
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        your_score += 1
        print("your total score: ", your_score)
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        your_score += 1
        print("your total score: ", your_score)
    else:
        print("You lose!")
        your_score -= 1
        print("your total score: ", your_score)
    #ask user if he wants to play again
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")