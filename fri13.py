#Max Low
#10-2-17
#fri13 -- find friday the 13 for next 10

from datetime import date
from calendar import weekday

month = date.today().month #defines month based on current month and stores as varible so it can be changed
year = date.today().year #defines month based on current month and stores as varible so it can be changed


i=0
while i< 10: #loop that runs until 10 fri13 are found 
    day = weekday(year,month,13) 
    """ defines a varible that finds the day of the week as a numerical value
    presets day to only look at the 13th's of each month"""
    if day == 4: #checks to see if the date is a friday
        print(month, '13', year) #prints off day if it meets restrictions of fri 13
        i+=1 #changes the amount of fri 13 found by one 
    month = month + 1 #changes to the next month to continue searching 
    if month >12: #can't have 13 months, resets if exceeding more months than in a year
        month = 1 #resets month to start of year if nessary
        year += 1 #increases year by one

