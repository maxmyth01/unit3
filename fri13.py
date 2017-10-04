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
year = date.today().year


i=0
while i< 10:
    day = weekday(year,month,13)
    print(month, '13', year)
    if day == 4:
        print('fri 13')
        i+=1
    month = month + 1 
    if month >=12:
        month = 0
        year += 1 
