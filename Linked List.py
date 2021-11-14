# Created by Huimin on 11/4/2021

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

# Insert just at exactly <location>
class SLinkedList:
    def __init__(self) : # constructor
        self.head = None
        self.tail = None
    def __iter__(self): # generator: returns the iterator object itself
        node = self.head
        while node:
            yield node #Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable 
            node = node.next
    def insertSLL(self, value, location):
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


                    
                    
                    





# Create two nodes SLL
singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)

singlyLinkedList.insertSLL(0,0)

singlyLinkedList.insertSLL(0,4)

""" node1 = Node(1)
node2 = Node(2)
singlyLinkedList.head = node1 # head is both the first node(with value, next attribute) itself and reference/address of the first node
singlyLinkedList.head.next = node2  # not node1.next?
singlyLinkedList.tail = node2 """

print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNode(1)
print([node.value for node in singlyLinkedList])

#print(singlyLinkedList.searchSLL(33))