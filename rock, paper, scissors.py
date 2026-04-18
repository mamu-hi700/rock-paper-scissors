import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif(
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'win'
    elif(
        (computer_choice == 'rock' and user_choice == 'scissors') or
        (computer_choice == 'scissors' and user_choice == 'paper') or
        (computer_choice == 'paper' and user_choice== 'rock')
    ):
        return 'lose'

def display_score(score):
    print(f'score:Wins - {score['win']} , Losses- {score['lose']},Draw - {score['draw']}')
    #score['win'] fetches the direct value from the dictionary

def main():
    print('---Welcome to the rock, paper, scissors game!!!---')
    print('If you chose to quit type "quit" ')
    print('Type reset to reset the game and scores ')

    score = {'win': 0,
             'lose': 0,
             'draw': 0
             }
    while True:
        user_choice = input('please enter your choice: ').lower()

        if user_choice == 'quit':
            print('---Thank you for playing---')
            break
        elif user_choice == 'reset':
            print('---The game is now reset---')
            score = {'win': 0,
             'lose': 0,
             'draw': 0
             }
            continue
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print('---Enter a valid response!!!---')
            continue

        computer_choice = get_computer_choice()

        print(f'You chose {user_choice}, the computer chose {computer_choice}')

        result = determine_winner(user_choice,computer_choice)
        print(f'You {result} this round')

        score[result] += 1

        display_score(score)

main()
    
