#Max Low
#10-2-17
#fri13 -- find friday the 13 for next 10

from datetime import date
from calendar import weekday

today = date.today().day, date.today().month, date.today().year
print(today)
day = weekday(date.today().year,date.today().month,date.today().day)
print(day)
month = date.today().month


i=0
while i< 5:
    day = weekday(date.today().year,month,13)
    print(day)
    if day == 4:
        print('fri 13')
        i+=1
    month = month + 1 
