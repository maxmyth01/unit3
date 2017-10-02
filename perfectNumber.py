#Max Low
#10-2-17
#perfectNumber.py -- determine if user input == perfect num

perfect = int(input('Enter a Number: '))

i=1
while i<= perfect:
    if perfect%i == 0:
        total = total+i
    i += 1
print(total)


