import random
elo = 0
while True:
    if elo < 200:
        print('')
        print('')
        print('')
        oPtion = str(input('rock paper or scissors (all lowercase): '))
        print('')


        if oPtion == 'rock':
            print('scissors')
            print('You Win!')
            elo += 10
        if oPtion == 'paper':
            print('rock')
            print('You Win!')
            elo += 10
        if oPtion == 'scissors':
            print('paper')
            print('You Win!')
            elo += 10
        print(f'Elo: {elo}')
        print('')
        print('')
        print('')
        
    if elo >= 200 and elo < 400:
        chance = random.randint(1, 100)
        if chance <= 10:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
        
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('scissors')
                print('You Win!')
                elo += 10
            if oPtion == 'paper':
                print('rock')
                print('You Win!')
                elo += 10
            if oPtion == 'scissors':
                print('paper')
                print('You Win!')
                elo += 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 400 and elo < 600:
        chance = random.randint(1, 100)
        if chance <= 30:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
            
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('scissors')
                print('You Win!')
                elo += 10
            if oPtion == 'paper':
                print('rock')
                print('You Win!')
                elo += 10
            if oPtion == 'scissors':
                print('paper')
                print('You Win!')
                elo += 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 600 and elo < 800:
        chance = random.randint(1, 100)
        if chance <= 50:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('scissors')
                print('You Win!')
                elo += 10
            if oPtion == 'paper':
                print('rock')
                print('You Win!')
                elo += 10
            if oPtion == 'scissors':
                print('paper')
                print('You Win!')
                elo += 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 800 and elo < 1000:
        chance = random.randint(1, 100)
        if chance <= 70:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
        
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('scissors')
                print('You Win!')
                elo += 10
            if oPtion == 'paper':
                print('rock')
                print('You Win!')
                elo += 10
            if oPtion == 'scissors':
                print('paper')
                print('You Win!')
                elo += 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 1000 and elo < 1200:
        chance = random.randint(1, 100)
        if chance <= 100:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
            
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('scissors')
                print('You Win!')
                elo += 10
            if oPtion == 'paper':
                print('rock')
                print('You Win!')
                elo += 10
            if oPtion == 'scissors':
                print('paper')
                print('You Win!')
                elo += 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 1200 and elo < 1400:
        chance = random.randint(1, 100)
        if chance <= 90:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
            
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('paper')
                print('You Win!')
                elo -= 10
            if input == 'paper':
                print('scissors')
                print('You Win!')
                elo -= 10
            if input == 'scissors':
                print('rock')
                print('You Win!')
                elo -= 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 1400 and elo < 1600:
        chance = random.randint(1, 100)
        if chance <= 70:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
            
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('paper')
                print('You Win!')
                elo -= 10
            if oPtion == 'paper':
                print('scissors')
                print('You Win!')
                elo -= 10
            if oPtion == 'scissors':
                print('rock')
                print('You Win!')
                elo -= 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 1600 and elo < 1800:
        chance = random.randint(1, 100)
        if chance <= 50:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
            
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('paper')
                print('You Win!')
                elo -= 10
            if oPtion == 'paper':
                print('scissors')
                print('You Win!')
                elo -= 10
            if oPtion == 'scissors':
                print('rock')
                print('You Win!')
                elo -= 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 1800 and elo < 2000:
        chance = random.randint(1, 100)
        if chance <= 30:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
            
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('paper')
                print('You Win!')
                elo -= 10
            if oPtion == 'paper':
                print('scissors')
                print('You Win!')
                elo -= 10
            if oPtion == 'scissors':
                print('rock')
                print('You Win!')
                elo -= 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')
    if elo >= 2000:
        chance = random.randint(1, 100)
        if chance <= 1:
            print('')
            print('')
            print('')
            rps_list = ['rock', 'paper', 'scissors']
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            rps = random.choice(rps_list)
            print('')

            if oPtion == rps:
                print(rps)
                print('tie')
            if oPtion == 'rock' and rps == 'paper':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'paper' and rps == 'scissors':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'scissors' and rps == 'rock':
                print(rps)
                print('I win')
                elo -= 10
            if oPtion == 'rock' and rps == 'scissors':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'scissors' and rps == 'paper':
                print(rps)
                print('You win')
                elo += 10
            if oPtion == 'paper' and rps == 'rock':
                print(rps)
                print('You win')
                elo += 10
            
            
            print(f'Elo: {elo}')
            
            print('')
            print('')
            print('')
        else:
            print('')
            print('')
            print('')
            oPtion = str(input('rock paper or scissors (all lowercase): '))
            print('')


            if oPtion == 'rock':
                print('paper')
                print('You Win!')
                elo -= 10
            if oPtion == 'paper':
                print('scissors')
                print('You Win!')
                elo -= 10
            if oPtion == 'scissors':
                print('rock')
                print('You Win!')
                elo -= 10
            
            print(f'Elo: {elo}')
            print('')
            print('')
            print('')