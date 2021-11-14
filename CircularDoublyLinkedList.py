# Created by Huimin on 11/5/2021

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self): # helps print out methods
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def createCDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node
     
    def insertCDLL(self, value, location):
        if self.head is None:
            return "CDLL doesn't exist."
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                newNode.prev = currNode
                newNode.next = currNode.next
                currNode.next = newNode
                newNode.next.prev = newNode

    def traverseCDLL(self):
        if self.head  is None:
            print("There is no ....")
        else:
            node = self.head
            while node:
                print(node.value)
                """ node = node.next
                if node == self.head:
                    break """
                if node == self.tail:
                    break
                node = node.next

    def reverseTraverseCDLL(self):
        if self.head is None:
            print("There is no ....")
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev

    def searchCDLL(self, value):
        if self.head is None:
            return "There is no such ...."
        else:
            node = self.head
            while node:
                if node.value == value:
                    return node.value
                """ if node == self.tail:
                    break
                node = node.next
            return "There is no...." """  # break + return = return
                if node == self.tail:
                    return "The value does not ...."
                node = node.next

    def deleteCDLL(self, location):
        if self.head  is None:
            print("There is no node ...")
        else:
            if location == 0:
                if self.tail == self.head:
                    self.head.prev = None
                    self.head.next = None
                    self.head == None
                    self.tail == None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.tail == self.head:
                    self.head.prev = None
                    self.head.next = None
                    self.head == None
                    self.tail == None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode

    def deleteEntireCDLL(self):
        if self.head is None:
            print("There is no...")
        else:
            self.tail.next = None # by setting this firstly, the loop will terminate naturally after last node
            node = self.head
            while node: 
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None

circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(1, -1)
circularDLL.insertCDLL(2, -1)
circularDLL.insertCDLL(3, -1)
circularDLL.insertCDLL(4, -1)
circularDLL.insertCDLL(5, -1)
circularDLL.insertCDLL(55, 5)

print([node.value for node in circularDLL])

circularDLL.traverseCDLL()
print()
circularDLL.reverseTraverseCDLL()
print()
print(circularDLL.searchCDLL(66))
print()
print([node.value for node in circularDLL])
print()
circularDLL.deleteCDLL(0)
print([node.value for node in circularDLL])
print()
circularDLL.deleteCDLL(-1)
print([node.value for node in circularDLL])
print()
circularDLL.deleteCDLL(1)
print([node.value for node in circularDLL])
print()
circularDLL.deleteEntireCDLL()
print([node.value for node in circularDLL])

