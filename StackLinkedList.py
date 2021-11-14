# Created by Huimin on 11/6/2021

from typing import no_type_check_decorator


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self) : # constructor
        self.head = None

    def __iter__(self): # generator: returns the iterator object itself
        node = self.head
        while node:
            yield node #Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable 
            node = node.next

class Stack:
    def __init__(self):
        self.linkedList = LinkedList() # no size limit
    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return "\n".join(values)

    def isEmpty(self):
        return self.linkedList.head == None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.linkedList.head
        self.linkedList.head = newNode

    def pop(self):
        if self.linkedList.head == None:
            return "There is no ..."
        else:
            value = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return value
            
    def peek(self):
        if self.linkedList.head == None:
            return "There is no ..."
        else:
            value = self.linkedList.head.value
            return value
            
    def delete(self):
        self.linkedList.head = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("------------")
print(customStack.pop())
print(customStack)