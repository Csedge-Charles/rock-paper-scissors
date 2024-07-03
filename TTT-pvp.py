import random
import time



for i in range(30):
    spot_1 = ' '
    spot_2 = ' '
    spot_3 = ' '
    spot_4 = ' '
    spot_5 = ' '
    spot_6 = ' '
    spot_7 = ' '
    spot_8 = ' '
    spot_9 = ' '

    tic = f' 1 | 2 | 3'
    tac = f' 4 | 5 | 6'
    toe = f' 7 | 8 | 9'
    line = '-----------'

    print(tic)
    print(line)
    print(tac)
    print(line)
    print(toe)

    spot_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]    

    running = True
    

    while running:



        if spot_1 == 'o' and spot_2 == 'o' and spot_3 == 'o':
            print('')
            print('')
            print('Player O Wins!')
            print('')
            print('')
            break
        if spot_4 == 'o' and spot_5 == 'o' and spot_6 == 'o':
            print('')
            print('')
            print('Player O Wins!')
            print('')
            print('')
            break
        if spot_7 == 'o' and spot_8 == 'o' and spot_9 == 'o':
            print('')
            print('')
            print('Player O Wins!')
            print('')
            print('')
            break
        if spot_1 == 'o' and spot_4 == 'o' and spot_7 == 'o':
            print('')
            print('')
            print('Player O Wins!')
            print('')
            print('')
            break
        if spot_2 == 'o' and spot_5 == 'o' and spot_8 == 'o':
            print('')
            print('')
            print('Player O Wins!')
            print('')
            print('')
            break
        if spot_3 == 'o' and spot_6 == 'o' and spot_9 == 'o':
            print('')
            print('')
            print('Player O Wins!')
            print('')
            print('')
            break
        if spot_1 == 'o' and spot_5 == 'o' and spot_9== 'o':
            print('')
            print('')
            print('Player O Wins!')
            print('')
            print('')
            break
        if spot_3 == 'o' and spot_5 == 'o' and spot_7 == 'o':
            print('')
            print('')
            print('Player O Wins!')
            print('')
            print('')
            break

        if spot_list == []:
            print('')
            print('')
            print('tie')
            print('')
            print('')
            break



        print('')
        print('')
        option = int(input('Select a spot: '))
        print('')
        print('')

        if option == 1:
            spot_list.remove(1)
            spot_1 = 'x'

        if option == 2:
            spot_list.remove(2)
            spot_2 = 'x'

        if option == 3:
            spot_list.remove(3)
            spot_3 = 'x'

        if option == 4:
            spot_list.remove(4)
            spot_4 = 'x'

        if option == 5:
            spot_list.remove(5)
            spot_5 = 'x'

        if option == 6:
            spot_list.remove(6)
            spot_6 = 'x'

        if option == 7:
            spot_list.remove(7)
            spot_7 = 'x'

        if option == 8:
            spot_list.remove(8)
            spot_8 = 'x'

        if option == 9:
            spot_list.remove(9)
            spot_9 = 'x'

        
        tic = f' {spot_1} | {spot_2} | {spot_3}'
        tac = f' {spot_4} | {spot_5} | {spot_6}'
        toe = f' {spot_7} | {spot_8} | {spot_9}'

        print(tic)
        print(line)
        print(tac)
        print(line)
        print(toe)

        if spot_1 == 'x' and spot_2 == 'x' and spot_3 == 'x':
            print('')
            print('')
            print('Player X Wins!')
            print('')
            print('')
            break
        if spot_4 == 'x' and spot_5 == 'x' and spot_6 == 'x':
            print('')
            print('')
            print('Player X Wins!')
            print('')
            print('')
            break
        if spot_7 == 'x' and spot_8 == 'x' and spot_9 == 'x':
            print('')
            print('')
            print('Player X Wins!')
            print('')
            print('')
            break
        if spot_1 == 'x' and spot_4 == 'x' and spot_7 == 'x':
            print('')
            print('')
            print('Player X Wins!')
            print('')
            print('')
            break
        if spot_2 == 'x' and spot_5 == 'x' and spot_8 == 'x':
            print('')
            print('')
            print('Player X Wins!')
            print('')
            print('')
            break
        if spot_3 == 'x' and spot_6 == 'x' and spot_9 == 'x':
            print('')
            print('')
            print('Player X Wins!')
            print('')
            print('')
            break
        if spot_1 == 'x' and spot_5 == 'x' and spot_9== 'x':
            print('')
            print('')
            print('Player X Wins!')
            print('')
            print('')
            break
        if spot_3 == 'x' and spot_5 == 'x' and spot_7 == 'x':
            print('')
            print('')
            print('Player X Wins!')
            print('')
            print('')
            break

        if spot_list == []:
            print('')
            print('')
            print('tie')
            print('')
            print('')
            break





        option = int(input('Select a spot Player O: '))
        print('')
        print('')



        if option == 1:
            spot_list.remove(1)
            spot_1 = 'o'

        if option == 2:
            spot_list.remove(2)
            spot_2 = 'o'

        if option == 3:
            spot_list.remove(3)
            spot_3 = 'o'

        if option == 4:
            spot_list.remove(4)
            spot_4 = 'o'

        if option == 5:
            spot_list.remove(5)
            spot_5 = 'o'

        if option == 6:
            spot_list.remove(6)
            spot_6 = 'o'

        if option == 7:
            spot_list.remove(7)
            spot_7 = 'o'

        if option == 8:
            spot_list.remove(8)
            spot_8 = 'o'

        if option == 9:
            spot_list.remove(9)
            spot_9 = 'o'

        tic = f' {spot_1} | {spot_2} | {spot_3}'
        tac = f' {spot_4} | {spot_5} | {spot_6}'
        toe = f' {spot_7} | {spot_8} | {spot_9}'

        print(tic)
        print(line)
        print(tac)
        print(line)
        print(toe)


