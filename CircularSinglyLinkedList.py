# Created by Huimin on 11/4/2021

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

# Insert just at exactly <location>
class CircularSinglyLinkedList:
    def __init__(self) : # constructor
        self.head = None
        self.tail = None
    def __iter__(self): # generator: returns the iterator object itself
        node = self.head
        while node:
            yield node #Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable 
            node = node.next
            if node == self.tail.next:
                break
            

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created."

    def insertCSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            else:
                if location == -1:
                    newNode.next = self.tail.next
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    newNode.next = nextNode
                    tempNode.next = newNode
            return "The node has been ...inserted."

    def traverseCSLL(self):
        if self.head is None:
            print("There is no....")
        else:
            node = self.head
            """ print(node.value)
            while node.next is not self.head:
                node = node.next
                print(node.value) """
            while node: # execution condition: node exits.
                print(node.value)
                node = node.next # increment
                if node is self.head: # termination condition, also node == self.tail.next
                    break
            
    def searchCSLL(self, value):
        if self.head is None:
            return "The CSLL is...."
        else:
            node = self.head
            while node:
                if node.value == value:
                    """ print(node.value)
                    break """
                    return node.value
                node = node.next
                if node == self.head: # when reaches this step, means we circle back to the first node without finding the value.
                    """ break
            print("The value doesn't exit.") """
                    return "The node does not exit." 
        
    def deleteCSLL(self, location):
        if self.head is None:
            return "There is no node."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None #?????
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None #?????
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail: # reach the node before the last node
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1: # reach the index before location
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireCSLL(self):
        self.head = None # setting the ref to be null, the link to the node disappears, and the original linked node is eligible for garbage collector
        self.tail.next = None
        self.tail = None



circularSLL = CircularSinglyLinkedList() 
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, -1)
circularSLL.insertCSLL(3, -1)
circularSLL.insertCSLL(4, -1)
#circularSLL.insertCSLL(44, 1)
print([node.value for node in circularSLL])

circularSLL.traverseCSLL()
""" print(circularSLL.searchCSLL(44)) """
circularSLL.deleteCSLL(2)
print([node.value for node in circularSLL])
circularSLL.deleteEntireCSLL()
print(circularSLL)
print([node.value for node in circularSLL])


"""     def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: # 0 based?
                newNode.next = self.head
                self.head = newNode
            elif location == 1: #end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                # traverse until tempNode is the node pror node at <location>
                while index < location - 1: 
                    tempNode = tempNode.next
                    index += 1 
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next= nextNode
        
    def traverseSLL(self):
        if self.head is None:
           print("The S L L does not exist.")
        else:
             node = self.head
             while node is not None: # execution condition
                 print(node.value)
                 node = node.next       
    def searchSLL(self, nodeValue):
        if self.head is None:
            print("The S L L does not exist.")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next  
            return 'The value does .....list'
    def deleteNode(self, location):
        if self.head is None:
            print('The S ... not exist.')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode is not None: # traverse all nodes
                        if tempNode.next == self.tail: # break while reach the second to last element
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while tempNode is not None:
                    if index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next # nextNode should be deleted
                    tempNode.next = nextNode.next

"""