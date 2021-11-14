# Created by Huimin on 11/6/2021

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)
    
    def isEmpty(self):
        return self.list == []

    def isFull(self):
        return len(self.list) == self.maxSize

    def push(self, value):
        if self.isFull():
            return "The ...full."
        else:
            self.list.append(value)
            return "The element...."

    def pop(self):
        if self.list == []:
            return "There is no..."
        else:
            return self.list.pop()

    def peek(self):
        if self.list == []:
            return "There is no..."
        else:
            return self.list[-1]

    # delete from memory
    def delete(self):
        self.list = None
        
customStack = Stack(3)
print(customStack.isEmpty())
print()
print(customStack.isFull())
print()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.isFull())
print()
print(customStack)
