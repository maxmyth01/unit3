#Max Low
#10-2-17
#perfectNumber.py -- determine if user input == perfect num

perfect = int(input('Enter a Number: '))

total = 0
i=1
while i< perfect:
    if perfect % i == 0:
        total = total + i
    i += 1
    
if total == perfect:
    print(perfect,'is a perfect number.')
else:
    print(perfect,'is not a perfect number.')


