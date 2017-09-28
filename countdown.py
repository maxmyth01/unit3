#Max Low
#9-28-17
#countdown.py -- countdown from user input until boom

num = int(input('Enter a number: '))

i=num
if i > 0:
    while i >= 0:
    print(i)
    i -= 1
else:
    print('Boom!')
