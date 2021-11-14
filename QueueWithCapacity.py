# Created by Huimin on 11/6/2021

class Queue:
    def __init__(self, maxSize):
        self.list = maxSize * [None] # This limits the size of list...but you can append value...does it limit the size?
        self.maxSize = maxSize # will use htis property to form circular functionality
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self): 
        return self.top == -1

    def enQueue(self, value):
        if self.isFull():
            return 'The queue is full...'
        elif self.start == -1: # check if the queue is empty
            self.start = 0
            self.top = 0
        else:
            self.top += 1
            if self.top == self.maxSize:
                self.top = 0 
        self.list[self.top] = value    
        return "The element is inserted.."

        """ else:
            if self.top + 1 == self.maxSize:
                self.top = 0 # logical index, not physical index, which is controlled by start and top index.
            else:
                self.top += 1
                if self.start == -1: # check if the queue is empty
                    self.start = 0
            self.list[self.top] = value
            return "The element is inserted..." """
    
    def deQueue(self):
        if self.isEmpty():
            return "The queue is empty.."
        else:
            firstElement = self.list[self.start]
            start = self.start
            if self.start == self.top: 
                self.start = -1
                self.top = -1
            else:
                self.start += 1
                if self.start == self.maxSize:
                    self.start = 0
                
            self.list[start] = None
            return firstElement

            """ if self.start == self.top: # class lecture: less clear
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            return firstElement """

    def peek(self):
        if self.isEmpty():
            return "The queue is empty.."
        else:
            return self.list[self.start]
        
    def delete(self):
        self.list = self.maxSize * [None] 
        self.start = -1
        self.top = -1

customQueue = Queue(3)
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
print(customQueue)
print()
print(customQueue.deQueue())
print()
print(customQueue.peek())
customQueue.delete()
print(customQueue)



