
class Stack:
    __stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        value = self.__stack[-1]
        del self.__stack[-1]
        return value


class AddingStak(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        self.__pop_count = 0

    def push(self, value):
        self.__sum += value
        Stack.push(self, value)

    def pop(self):
        value = Stack.pop(self)
        self.__sum -= value
        self.__pop_count += 1
        return value

    def get_sum(self):
        return self.__sum

    def get_counter(self):
        return self.__pop_count

s = AddingStak()
s.push(1)
s.push(2)
s.push(3)

#print(s.__stack)
print("sum =", s.get_sum())

print(s.pop())
print(s.pop())
print(s.pop())

print("pop count =", s.get_counter())