#Max Low
#10-2-17
#warmup8.py -- find the sum of all intigers less than 100,000 that are divisible by 3, 10, and 17

total=0
i=0
while i <= 100000:
    if i %(3*10*17) ==0:
        total = total + i
    i+= 1
print(total)

