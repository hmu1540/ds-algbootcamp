# Created by Huimin on 11/6/2021

class Queue():
    def __init__(self):
        self.list = [] # no size limit
    
    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)

    def isEmpty(self):
        return self.list == []

    def enQueue(self, value):
        self.list.append(value)
        print("The element....end of the queue")

    def deQueue(self):
        if self.isEmpty():
            return "There is no ..."
        else:
            return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is no ..."
        else:
            return self.list[0]

    def delete(self):
        self.list = None

customQueue = Queue()
print(customQueue.isEmpty())
print()
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
customQueue.enQueue(4)
customQueue.enQueue(5)
print(customQueue.peek())
customQueue.delete()
print(customQueue)