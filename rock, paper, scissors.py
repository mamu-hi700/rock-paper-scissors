import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

print("--- Welcome to the Best of 3 Challenge! ---")

while user_wins < 2 and computer_wins < 2:
    user_input = input("Choose Rock, Paper, or Scissors (or Q to quit): ").lower()
    
    if user_input == "q":
        break
    if user_input not in options:
        print("Invalid move, try again.")
        continue

    computer_pick = random.choice(options)
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("It's a tie!")
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        print("You won this round!")
        user_wins += 1
    else:
        print("Computer won this round!")
        computer_wins += 1

    print(f"Score -> You: {user_wins} | Computer: {computer_wins}\n")

if user_wins > computer_wins:
    print("CONGRATULATIONS! You won the match!")
else:
    print("The computer won the match. Better luck next time!")