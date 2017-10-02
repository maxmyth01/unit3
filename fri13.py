#Max Low
#10-2-17
#fri13 -- find friday the 13 in the next 10 years

from datetime import date
from calendar import weekday

today = date.today().day, date.today().month, date.today().year
print(today)
day = weekday(date.today().year,date.today().month,date.today().day)
print(day)