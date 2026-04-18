import random

number_to_guess = random.randint(1,100)
attempt = 0
max_attempt = 3

print('---Welcome to the Guessing Game!---')

while attempt < max_attempt:
    try:
        userChoice = input(f'Attempt {attempt + 1}/{max_attempt}-Guess the number between (1-100):  ')
        guess = int(userChoice)

        #increase immediately a valid number is entered 
        attempt += 1

        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!!')
        else:
            print(f'Congratulations!, you  guesed correctly in {attempt} tries')
            break #exiting the loop because user has won
    except ValueError:
        print('Enter a valid number!!')
if attempt == max_attempt:
    print('---GAME OVER---')
    print(f'The magic number was : {number_to_guess}')

