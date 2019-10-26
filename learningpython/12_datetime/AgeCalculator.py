"""
NSF - CODING - Date & Time
"""

import datetime


myBirthDate = datetime.datetime(2009, 8, 20)

today = datetime.date.today()

age = today.year - myBirthDate.year

print(age)
