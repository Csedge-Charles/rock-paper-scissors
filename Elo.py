import random
elo = 0
if elo < 200:
    print('')
    print('')
    print('')
    rps_list = ['rock', 'paper', 'scissors']
    input = str(input('rock paper or scissors (all lowercase): '))
    rps = random.choice(rps_list)
    print('')

    if input == rps:
        print(rps)
        print('tie')
    if input == 'rock' and rps == 'paper':
        print(rps)
        print('I win')
    if input == 'paper' and rps == 'scissors':
        print(rps)
        print('I win')
    if input == 'scissors' and rps == 'rock':
        print(rps)
        print('I win')
    if input == 'rock' and rps == 'scissors':
        print(rps)
        print('You win')
    if input == 'scissors' and rps == 'paper':
        print(rps)
        print('You win')
    if input == 'paper' and rps == 'rock':
        print(rps)
        print('You win')
    else:
        print('Invalid Answer')
    print('')
    print('')
    print('')