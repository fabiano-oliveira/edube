
from typing import Type


class TimeInterval:
    def __init__(self, *, hours = 0, minutes = 0, seconds = 0):
        if not isinstance(hours, int):
            raise TypeError(hours)
        if not isinstance(minutes, int):
            raise TypeError(minutes)
        if not isinstance(seconds, int):
            raise TypeError(seconds)

        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
        self.__equalize()


    def __equalize(self):
        if self.__seconds >= 60:
            self.__seconds -= 60
            self.__minutes += 1
        elif self.__seconds < 0:
            self.__minutes -= 1
            self.__seconds += 60

        if self.__minutes >= 60:
            self.__minutes -= 60
            self.__hours += 1
        elif self.__minutes < 0:
            self.__hours -= 1
            self.__minutes += 60

    def gethours(self) -> int:
        return self.__hours

    def getminutes(self) -> int:
        return self.__minutes

    def getseconds(self) -> int:
        return self.__seconds

    def __add__(self, x):
        if isinstance(x, TimeInterval):
            return TimeInterval(
                hours=self.__hours + x.gethours()
                , minutes=self.__minutes + x.getminutes()
                , seconds=self.__seconds + x.getseconds()
            )
        elif isinstance(x, int):
            return TimeInterval(
                hours=self.__hours
                , minutes=self.__minutes
                , seconds=self.__seconds + x
            )
        else:
            raise TypeError(x)

    def __sub__(self, x):
        if isinstance(x, TimeInterval):
            return TimeInterval(
                hours=self.__hours - x.gethours()
                , minutes=self.__minutes - x.getminutes()
                , seconds=self.__seconds - x.getseconds()
            )
        elif isinstance(x, int):
            return TimeInterval(
                hours=self.__hours
                , minutes=self.__minutes
                , seconds=self.__seconds - x
            )
        else:
            raise TypeError(x)

    def __mul__(self, x):
        return TimeInterval(
            hours=self.__hours * x
            , minutes=self.__minutes * x 
            , seconds=self.__seconds * x
        )

    def __str__(self) -> str:
        return f'{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}'

