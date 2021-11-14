# Created by Huimin on 11/6/2021

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self) : # constructor
        self.head = None
        self.tail = None

    def __iter__(self): # generator: returns the iterator object itself
        node = self.head
        while node:
            yield node #Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable 
            node = node.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)

    def enQueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            newNode.next = None
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        return self.linkedList.head == None
    
    def deQueue(self):
        if self.linkedList.head == None:
            return "The queue has no node..."
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode # will return what __str__ returns, the value

    def peek(self):
        if self.linkedList.head == None:
            return "The queue has no node."
        else:
            return self.linkedList.head
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

""" customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
print(customQueue)
print(customQueue.isEmpty())
print()
print(customQueue.deQueue())
print(customQueue.peek()) """
