#Max Low
#10-4-17
#betterAdditionGameDemo.py -- ask addtion problems till user gets 5 right

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question  = 'what is' + str(num1) + '+' + str(num2) + '?'
    answer = int(input(question))
    if answer == num1+num2:
        numCorrect += 1
    else:
        print('The answer was', num1+num2)
print('Congratulations! You win! ')
