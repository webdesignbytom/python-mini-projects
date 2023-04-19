name = input('Enter your name: ')
print('Welcome', name, 'to the adventure!')

answer = input('Do you get up or go to sleep? (y/n): ').lower()

if answer == 'y':
    answer = input('You go to the kitten do you cook or drink? ').lower()
    if answer == 'cook':
        print('mmm bacon')
    elif answer == 'drink':
        print('yum booze')
    else: 
        print('Not a valid answer')

if answer == 'n':
    answer = input('Do you sleep or nap ').lower()
    if answer == 'sleep':
        print('Yea just few more hours')
    elif answer == 'nap':
        print('20 mins tops')
    else: 
        print('Not a valid answer')