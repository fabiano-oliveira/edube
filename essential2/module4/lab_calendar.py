import calendar
from datetime import datetime, date
import random


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year:int, weekday:int):
        count = 0

        for month in self.yeardays2calendar(year):
            for week_groups in month:
                for week in week_groups:
                    for (day, wd) in week:
                        if wd == weekday and day > 0:
                            count += 1

        return count

c = MyCalendar()
print(c.count_weekday_in_year(2019, 0))
print(c.count_weekday_in_year(2000, 6))

b = bytearray(3)
print(b)

x = [0, 2, 7]
print([i ** 2 for i in x])

d1 = datetime(2019, 11, 27, 11, 27, 22)
d2 = datetime(2019, 11, 27, 0, 0, 0)
print(d1 - d2)

d1 = date(1992, 1, 16)
d2 = date(1991, 2, 5)
print(d1 - d2)