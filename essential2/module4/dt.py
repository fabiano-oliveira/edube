from datetime import datetime, time
import calendar


print('today', datetime.today().date())
print('now', datetime.now())
print('utcnow', datetime.utcnow())

dt = datetime(2020, 11, 4, 14, 53)
print('-----')
print(dt)
print(dt.strftime('%Y/%m/%d %H:%M:%S'))
print(dt.strftime('%y/%B/%d %H:%M:%S %p'))
print(dt.strftime('%a, %Y %b %d'))
print(dt.strftime('Weekday: %w'))
print(dt.strftime('Day of the year: %j'))
print(dt.strftime('Week number of the year: %U'))

print('-------')
t = time(14, 39)
print(t.strftime('%H:%M:%S'))

print('------')
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.calendar(2021, w = 3, m = 4))
print(calendar.month(2021, 3))