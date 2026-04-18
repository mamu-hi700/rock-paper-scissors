import random

roll_count = 0
while True:
    choice = input('Roll the dice? (y/n)  ').lower()
#THE ACTION OF THE CODE
    if choice == 'y':
        try:
            dice_choice = int(input('Enter the number of dice you want to roll: '))
            rolls = []
            for i in range(dice_choice):
                rolls.append(random.randint(1,6))
#DISPLAY THE RESULT CONVERTED TO A TUPLE
            print(tuple(rolls))
#INCREASE THE COUNTER
            roll_count += 1
            print(f'Total roll in this session: {roll_count}')

        except ValueError:
        #THIS PREVENTS THE PROGRAM FROM CRASHING INCASE THE USER ENTERS THE WRO
            print('Please enter a whole valid number for the dice count')
    elif choice == 'n':
        print('Thank you for playing')
        print(f'Final roll count: {roll_count}')
        break
    else:
        print('Invalid input'.title())
