#Max Low
#9-28-17
#gauss.py -- count the numbers as a series, user control start, stop and intervil

start = int(input('Enter a starting value: '))
end = int(input('Enter a final value: '))
step = int(input('Enter the step: '))

i=1
while i <= end:
    total = total + i
    i = i + step
    print(total)

