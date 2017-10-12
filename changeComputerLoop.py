#Max Low
#10-5-17
#changeComputer.py convert to change with loop

change = int(input('Enter an amount of change: '))
q= 0
d= 0
n= 0
p= 0

while change > 25:
    change = change - 25 
    q += 1
    
while change > 10:
    change = change - 10
    d += 1
    
while change > 5:
    change = change - 5
    n += 1
    
while change >= 1:
    change = change - 1
    p += 1
    
print(q, d, n, p)
    

    