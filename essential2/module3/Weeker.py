
"""
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you - this name comes from the fact that objects of that class will be able to store and to manipulate days of a week.

The class constructor accepts one argument - a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
all object's properties should be private;
"""

class WeekDayError(Exception):
    pass

class Weeker:
    __weekdays = [ "Mon", "Tue", "Web", "Thu", "Fri", "Sat", "Sun" ]

    def __init__(self, wd: str) -> None:
        if wd not in Weeker.__weekdays:
            raise WeekDayError(f"{wd} is an invalid weekday.")
        
        self.__day = Weeker.__weekdays.index(wd)
    
    def __str__(self) -> str:
        return Weeker.__weekdays[self.__day]

    def add_days(self, n: int) -> None:
        self.__day += n % 7
        if self.__day >= 7:
            self.__day -= 7

    def subtract_days(self, n: int) -> None: 
        self.__day -= n % 7
        if (self.__day < 0):
            self.__day += 7

try:
    w_err = Weeker("Fab")
except WeekDayError:
    print("Dia inválido")

wd = Weeker("Mon")
print(wd)
print(wd.__dict__)

print("++")
wd.add_days(1)
print(wd)
wd.add_days(9)
print(wd)
wd.add_days(4)
print(wd)

print("--")
wd.subtract_days(2)
print(wd)