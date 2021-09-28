
class QueueError(Exception):
    pass

class Queue:
    __queue = []


    def put(self, element):
        self.__queue.append(element)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError("The queue is empty.")

        element = self.__queue[0]
        del self.__queue[0]
        return element

class SuperQueue(Queue):

    __count = 0

    def put(self, element):
        Queue.put(self, element)
        self.__count += 1

    def get(self):
        self.__count -= 1
        return Queue.get(self)
        
    def isempty(self):
        return self.__count == 0

q = SuperQueue()
q.put(1)
q.put("dog")
q.put(False)
q2 = SuperQueue()
q2.put(2)


print(q.__dict__)
print(q2.__dict__)

try:
    for i in range(4):
        if not q.isempty():
            print(q.get())
        else:
            print("Queue empty.")
except QueueError as err:
    print(err)

print(q.__dict__)
print(q2.__dict__)

print(q2.get())