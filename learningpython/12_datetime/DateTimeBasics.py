"""
NSF - CODING - Date & Time
"""

import datetime

today = datetime.date.today()

print(today)

#prints today's / current date in the format YYYY-MM-DD (example: 2018-10-17)

print('Year : ' + str(today.year))

print('Month: ' + str(today.month))

print('Day: ' + str(today.day))

"""
Output of this program
2018-10-17
Year : 2018
Month: 10
Day: 17
"""

nowdate = datetime.datetime.now()
print(nowdate)

#2018-10-17 21:36:39.043546