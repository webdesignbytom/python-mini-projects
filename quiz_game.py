print('Welcome to my computer quiz!')

playing = input('Do you want to play the game? (y/n) ')

if playing.lower() != 'y':
    quit()

print('Ok lets play')
score = 0;

answer = input('whats does cpu stand for? ').lower()
if answer == 'central processing unit':
    print('correct!')
    score += 1
else:
    print('wrong answer')

answer = input('whats does gpu stand for? ').lower()
if answer == 'graphics processing unit':
    print('correct!')
    score += 1
else:
    print('wrong answer')

answer = input('whats does ram stand for? ').lower()
if answer == 'random access memory':
    print('correct!')
    score += 1
else:
    print('wrong answer')

answer = input('whats does a computer do? ').lower()
if answer == 'count':
    print('correct!')
    score += 1
else:
    print('wrong answer')

print('You got ' + str(score) + ' questions right!')
print('You got ' + str((score/4) * 100) + ' percent right!')

print('...')