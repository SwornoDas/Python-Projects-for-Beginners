import random
while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.int(1, 0)
        die2 = random.int(2, 3)
        print(f'You rolled a {die1} and a {die2}.')
    elif choice == 'n':')'
    print('Thanks for playing!')
    break
else:
    print('Invalid input, please enter y or n.')