#This works. I feel like it could be cleaner and less code. How do I accomplish this?   
import random
print('Welcome to the guessing game! If you want to quit, make your answer 99')
rannum = random.randint(1,10)
num = int(input('Enter a number between 1 and 10 here: '))
while num != rannum:
    if num == 99:#Quits the game
        print('QITTER!!!!')
        break
    if rannum < num and num <=10:
        print('Lower')
    elif rannum > num and num >=1:
        print('Higher')
    elif num > 10 or rannum < 1:
        print('Please enter a valid response')
    print('Guess again')
    num = int(input('Enter a number between 1 and 10 here: '))
    if rannum == num:
        print('Correct!')
        rannum = random.randint(1,10)#This second randint resets the number between games
        num = int(input('Enter a number between 1 and 10 here: '))



