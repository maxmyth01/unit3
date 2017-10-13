#Max Low
#10-13-17
#quiz3.py -- numbers -5:5 for loop, 18:32 by 2 while loop, odd sum of numbers 13:331, asks for word until it contains z

for i in range(-5,5):
    print(i)
    
j = 18
while j <= 32:
    print(j)
    j += 2

q = 13
total = 0
while q <= 331:
    total = total + q
    q +=2 
print(total)
    
word = input('Enter a word')
if 'z' in word:
    print(word)
else:
    word = input('Enter a word')
