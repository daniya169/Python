#try
#except
#finally

while True:
    try:
        age=int(input('Enter your age:'))
        break
    except ValueError:
        print('Try Again')

    finally:
        print('You have enter the correct data')

if age<18:
    print("you can't play the game ")

else:
    print('you can play the game')
