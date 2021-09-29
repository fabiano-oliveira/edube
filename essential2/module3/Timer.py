
"""
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.
Use the following hints:

all object's properties should be private;
consider writing a separate function (not method!) to format the time string.
"""

class Timer:

    def __init__(self, hour, minute = 0, second = 0) -> None:
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self) -> str:
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

    def next_second(self):
        self.__second += 1
        if self.__second >= 60:
            self.__second = 0
            self.__minute += 1

            if self.__minute >= 60:
                self.__minute = 0
                self.__hour += 1

                if self.__hour >= 24:
                    self.__hour = 0

    def previous_second(self):
        self.__second -= 1
        if self.__second < 0:
            self.__second = 59
            self.__minute -= 1

            if self.__minute < 0:
                self.__minute = 59
                self.__hour -= 1

                if self.__hour < 0:
                    self.__hour = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)
timer.previous_second()
print(timer)