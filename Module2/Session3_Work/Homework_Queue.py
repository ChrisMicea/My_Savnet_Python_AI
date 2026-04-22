class QueueError(Exception):
    pass

class MyQueue():
    def __init__(self):
        self.__queueList = []

    def put(self, elem):
        self.__queueList.append(elem)
        
    def get(self):
        if len(self.__queueList) == 0:
            raise QueueError("Queue is empty -- cannot get element")

        elem = self.__queueList[0]
        del self.__queueList[0]
        return elem

    def is_empty(self):
        return len(self.__queueList) == 0

    def __str__(self):
        return str(self.__queueList)

q = MyQueue()
print(q)
q.put(1)
print(q)
q.put(2)
print(q)
q.put(3)
print(q)
print(q.get())
print(q)
print(q.get())
print(q)
print(q.get())
print(q)
try:
    print(q.get())
except QueueError as e:
    print(e)
print(q.is_empty())
