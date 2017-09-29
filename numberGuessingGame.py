#Max Low
#9-29-17
#numberGuessingGame.py -- guess a number then display eventual 

from random import randint

guess = int(input('Guess a number between 1-100: '))
num = randint(1,100)
total = 0

while num != guess:
    if guess > num:
        print('Too high')
    if guess < num:
        print('Too low')
    total += 1
    guess = int(input('Guess a number between 1-100: '))

print('You win')
    
    
