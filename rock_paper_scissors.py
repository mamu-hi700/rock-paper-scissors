import random

def get_computer_choice() -> str:
    '''selects a random move for the computer'''
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def determine_winner(user: str, computer: str) -> str:
    '''Determine the result of a single round'''
    if user == computer:
        return 'tie'
    
    win_conditions = {
        'rock' : 'scissors',
        'paper' : 'rock',
        'scissors' : 'paper'
    }

    if win_conditions[user] == computer:
        return 'user'
    return 'computer'

def handle_commands(user_input: str) -> str:
    '''checks if user wants to quit or reset'''
    if user_input == 'q':
        print('Thanks for playing! Goodbye.')
        exit() # Thsi stops the script
    elif user_input == 'r':
        print('\n--- Scores Reset! Starting over... ---\n')
        return 'reset'
    return 'continue'

def play_game():
    'Main game loop for the Best of Three'
    user_wins = 0
    computer_wins = 0

    print('---Professional Rock Paper Scissors')

    while user_wins < 2 and computer_wins < 2:
        user_choice = input("Enter 'r' to reset and 'q' to quit. \n Enter Choice:  ").lower()

        status = handle_commands(user_choice)

        if status == 'reset':
            user_wins = 0
            computer_wins = 0
            continue

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input, please try again.")
            continue

        
        # Get the computer's move
        comp_choice = get_computer_choice()
        print(f'Computer Choice: {comp_choice}')

        # Get winner from the judge
        result = determine_winner(user_choice , comp_choice)

        # updating the scores 
        if result == 'user':
            print('you won that round')
            user_wins += 1
        elif result == 'computer':
            print('computer won that round!')
            computer_wins += 1
        else:
            print("It's a tie!")


if __name__ == '__main__':
    play_game()