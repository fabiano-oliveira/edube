
class ExampleClass:
    counter = 0

    def __init__(self, value = 1):
        self.__first = value
#        self.counter = 0
        ExampleClass.counter += 1

    def inc(self):
        self.counter += 1

e1 = ExampleClass()
e2 = ExampleClass(2)
e3 = ExampleClass(3)

print(e3.__dict__)
print("counter =", e3.counter)

e3.inc()
print(e3.__dict__)
print("counter =", e3.counter)