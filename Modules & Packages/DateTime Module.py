##Use the `datetime` module to print the current date, calculate the date 100 days from today, and determine the day of the week for a given date.

import datetime

Date = datetime.date.today()
print(Date)

print(Date + datetime.timedelta(days=100))

D = datetime.date(2026,3,1)
day = D.strftime('%A')
print(day)

