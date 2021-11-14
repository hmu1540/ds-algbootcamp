# Created by Huimin on 11/5/2021

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self): # helps print out methods
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The ... created"

    def insertDLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.mext
                    index += 1
                nextNode = tempNode.next
                newNode.prev = tempNode
                newNode.next = nextNode
                tempNode.next = newNode
                nextNode.prev = newNode

    def traverseDLL(self):
        if self.head is None:
            print("There is no node ...")
        else:
            node = self.head
            while node:
                print(node.value)
                """ if node == self.tail: # no need of this if block, b/c while node: excution rule reaching the last node.
                    break """
                node = node.next
                  
    def reverseTraverseDLL(self):
        if self.tail is None:
            print("There is no node...")
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev

    def searchDLL(self, value):
        if self.head is None:
            return "There is no such node..."
        else:
            node = self.head
            while node:
                if node.value == value:
                    return node.value
                node = node.next
            return "There is no such node"

    def deleteDLL(self, location):
        if self.head is None:
            print("There is no ....")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                tempNode.next.prev = tempNode

    def deleteEntireDLL(self):
        if self.head is None:
            print("There is no ....")
        else:
            node = self.head
            while node:             
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None
            print("The entire DLL ....")


doublyLL = DoublyLinkedList()
#doublyLL.createDLL(5)
doublyLL.insertDLL(1, -1)
doublyLL.insertDLL(2, -1)
doublyLL.insertDLL(3, -1)
doublyLL.insertDLL(4, -1)
doublyLL.insertDLL(55, 1)

print([node.value for node in doublyLL])
doublyLL.traverseDLL()
doublyLL.reverseTraverseDLL()
print(doublyLL.searchDLL(55))
doublyLL.deleteDLL(-1)
print([node.value for node in doublyLL])
doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])


