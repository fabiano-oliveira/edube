
class Fib:

    def __init__(self, n) -> None:
        self.__n = n
        self.__current_number = self.__next_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__n <= 0:
            raise StopIteration

        self.__n -= 1
        current = self.__current_number
        if current == 0:
            self.__current_number = 1
            self.__next_number = 1
        else: 
            self.__current_number, self.__next_number = self.__next_number, self.__current_number + self.__next_number

        return current

def fibonacci(n):
    curent = 0
    next = 0

    for i in range(n):
        yield curent

        if next == 0:
            curent = next = 1
        else:
            curent, next = next, curent + next


print(list(Fib(10)))
print(list(fibonacci(15)))