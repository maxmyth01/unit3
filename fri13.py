#Max Low
#10-2-17
#fri13 -- find friday the 13 for next 10

from datetime import date
from calendar import weekday

today = date.today().day, date.today().month, date.today().year
print(today)
day = weekday(date.today().year,date.today().month,date.today().day)
print(day)

"""
i=0
while i< 1:
    day = weekday(date.today().year,date.today().month,13)
print(day)
    if day == 4 and date.today().day == 13:
        print(today)
        i+=1
"""