#This works!!!!!
import random
print('Welcome to the guessing game! If you want to quit, make your answer 99')
rannum = random.randint(1,10)
num = int(input('Enter a number between 1 and 10 here: '))
while num != rannum:
    if num == 99:
        print('QITTER!!!!')
        break
    if rannum < num:
            print('Lower')
    elif rannum > num:
            print('Higher')
    print('Guess again')
    num = int(input('Enter a number between 1 and 10 here: '))
    if rannum == num:
        print('Correct!')
        rannum = random.randint(1,10)
        num = int(input('Enter a number between 1 and 10 here: '))




