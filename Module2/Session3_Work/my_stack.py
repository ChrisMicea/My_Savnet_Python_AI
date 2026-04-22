class StackError(Exception):
    pass

class MyStack:
    def __init__(self) -> None:
        self.__stackList = []

    def push(self, item):
        self.__stackList.append(item)

    def pop(self):
        if len(self.__stackList) == 0:
            raise StackError("Stack is empty -- cannot pop element")
        item = self.__stackList[-1]
        # self.__stackList.remove(self.__stackList[-1])
        # self.__stackList.remove(item)
        del self.__stackList[-1]
        return item
    
    def __str__(self):
        # [::-1] in order for the printed elements to be in stack order - LIFO
        return str(self.__stackList[::-1]) 

# st = MyStack()
# st.push(1)
# st.push(2)
# st.push(3)
# print(st)
# # print(st.pop())
# # print(st.pop())
# # print(st.pop())
# st.pop()
# print(st)

class AddingStack(MyStack):
    def __init__(self) -> None:
        super().__init__()
        self.__sum = 0
    
    def get_sum(self):
        return self.__sum
    
    def push(self, item):
        self.__sum += item
        super().push(item)
    
    def pop(self):
        item = super().pop()
        self.__sum -= item
        return item

# addSt = AddingStack()
# addSt.push(1)
# addSt.push(2)
# addSt.push(3)
# print(addSt)
# print(addSt.get_sum())
# addSt.pop()
# print(addSt)
# print(addSt.get_sum())

class CountingStack(MyStack):
    def __init__(self) -> None:
        super().__init__()
        self.__counter = 0
    
    def get_counter(self):
        return self.__counter
    
    def push(self, item):
        self.__counter += 1
        super().push(item)
    
    def pop(self):
        self.__counter -= 1
        return super().pop()

cntSt = CountingStack()
cntSt.push(1)
cntSt.push(2)
cntSt.push(3)
print(cntSt)
print(cntSt.get_counter())
cntSt.pop()
cntSt.pop()
print(cntSt)
print(cntSt.get_counter())
cntSt.pop()
cntSt.pop()