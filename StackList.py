# Create by Huimin on 11/6/2021


class Stack:
    def __init__(self):
        self.list = [] # no size limit
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)
    
    def isEmpty(self):
        return self.list == []

    def push(self, value):
        self.list.append(value)
        print("The element....")

    def pop(self):
        if self.list == []:
            return "There is no..."
        else:
            return self.list.pop()

    def peek(self):
        if self.list == []:
            return "There is no .."
        else:
            return self.list[-1]

    # delete all elements   
    def delete(self):
        if self.list == []:
            return "There is no..."
        else:
            self.list.clear() 
            
    # delete from memory
    def delete2(self):
        self.list = None

customStack = Stack()
print(customStack.isEmpty())
print()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)

print(customStack)
print()
print(customStack.pop())
print()
print(customStack)
print()
print(customStack.peek())
print()
print(customStack.pop())
print()
print(customStack)
print()
print(customStack.peek())