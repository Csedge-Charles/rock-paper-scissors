#Play Command line Rock-Paper-Scissors
#All inputs should be in lowercase
#Play Rock-Paper-Scissors against AI
#Ranked 1st in the world 



import random

text = '''  ___    ___ ________  ___  ___          ___       __   ________  ________      
 |\  \  /  /|\   __  \|\  \|\  \        |\  \     |\  \|\   __  \|\   ___  \    
 \ \  \/  / | \  \|\  \ \  \\\  \       \ \  \    \ \  \ \  \|\  \ \  \\ \  \   
  \ \    / / \ \  \\\  \ \  \\\  \       \ \  \  __\ \  \ \  \\\  \ \  \\ \  \  
   \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ 
 __/  / /      \ \_______\ \_______\       \ \____________\ \_______\ \__\\ \__\
|\___/ /        \|_______|\|_______|        \|____________|\|_______|\|__| \|__|
\|___|/'''                                                                       
                                                                        
text_2 = ''' ___          ___       __   ________  ________      
|\  \        |\  \     |\  \|\   __  \|\   ___  \    
\ \  \       \ \  \    \ \  \ \  \|\  \ \  \\ \  \   
 \ \  \       \ \  \  __\ \  \ \  \\\  \ \  \\ \  \  
  \ \  \       \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ 
   \ \__\       \ \____________\ \_______\ \__\\ \__\
    \|__|        \|____________|\|_______|\|__| \|__|
                                                     
                                                    '''


mode = int(input('best of 1 or 3: '))
if mode == 1:
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
if mode == 3:
    point_AI = 0
    point_Player = 0
    while point_AI != 2 or point_Player != 2:
        if point_AI == 2 or point_Player == 2:
            break
        print('')
        print('')
        print('')
        rps_list = ['rock', 'paper', 'scissors']
        inp = (input('rock paper or scissors (all lowercase): '))
        rps = random.choice(rps_list)
        print('')

        if inp == rps:
            print(rps)
            print('tie')
        elif inp == 'rock' and rps == 'paper':
            print(rps)
            print('I win')
            point_AI += 1
        elif inp == 'paper' and rps == 'scissors':
            print(rps)
            print('I win')
            point_AI += 1
        elif inp == 'scissors' and rps == 'rock':
            print(rps)
            print('I win')
            point_AI += 1
        elif inp == 'rock' and rps == 'scissors':
            print(rps)
            print('You win')
            point_Player += 1
        elif inp == 'scissors' and rps == 'paper':
            print(rps)
            print('You win')
            point_Player += 1
        elif inp == 'paper' and rps == 'rock':
            print(rps)
            print('You win')
            point_Player += 1
        else:
            print('Invalid Answer')
        print('')
        print('')
        print(f'Me: {point_AI}   You: {point_Player}')
        print('')
    if point_AI == 2:
        print(text_2)
    if point_Player == 2:
        print(f"{text}")

