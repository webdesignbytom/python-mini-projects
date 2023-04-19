import random

top_of_range = input('Enter a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number larger than 0')
        quit()
else:
    print('Please enter a number')
    quit()

random_number = random.randint(0, top_of_range)
# print('random number', random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Enter a number')
        continue
    
    if user_guess == random_number:
        print('You got It!')
        break
    elif user_guess > random_number:
        print('youre above the number')
    else: 
        print('youre below the number')

print('You got it in', guesses, 'guesses')