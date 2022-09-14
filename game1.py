win_num=45
num=int(input('Enter the number:'))

Game_over=False

while not Game_over:

    if num==win_num:
        print('You Won!!!')
        Game_over=True

    else:
        if num<win_num:
            print('Too LOw')
            num=int(input('Enter the number Again:'))

        else:
            print('Too High')
            num=int(input('Enter the number Again:'))
