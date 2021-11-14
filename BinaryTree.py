# Created by Huimin on 11/7/2021

from typing import NewType


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrderTraversal(rootNode):
    if not rootNode: # termination condition
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

#preOrderTraversal(newBT)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

#inOrderTraversal(newBT)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
import QueueLinkedList as queue

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()     
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enQueue(root.value.leftChild)        
            if (root.value.rightChild is not None):
                customQueue.enQueue(root.value.rightChild)

#levelOrderTraversal(newBT) 

def searchBT(rootNode, value):
    if rootNode is None:
        return "The BT ...exist."
    else:
        customQueue = queue.Queue()     
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            if root.value.data == value:
                return "success"
            if (root.value.leftChild is not None):
                customQueue.enQueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enQueue(root.value.rightChild)
        return "Not found"

#print(searchBT(newBT, "Cold"))
#print(searchBT(newBT, "tea"))

def insertBT(rootNode, newNode):
    # find the first node without two children and its first vacant place: left or right.
    if rootNode is None: # or not rootNode
        rootNode = newNode
    else:
        customQueue = queue.Queue()     
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            if (root.value.leftChild is not None):
                customQueue.enQueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "successfully inserted"
            if (root.value.rightChild is not None):
                customQueue.enQueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "successfully inserted"

""" newNode = TreeNode("Cola")
print(insertBT(newBT, newNode))
levelOrderTraversal(newBT) """

def getDeepestNodeBT(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()     
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            if (root.value.leftChild is not None):
                customQueue.enQueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enQueue(root.value.rightChild)
        deepestNode =  root.value              
        return deepestNode

def deleteDeepestNodeBT(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()     
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            if root.value == dNode:
                root.value = None
                return
            if root.value.leftChild:
                if root.value.leftChild == dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enQueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild == dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enQueue(root.value.rightChild)

# newNode = getDeepestNodeBT(newBT)
# deleteDeepestNodeBT(newBT, newNode)
# levelOrderTraversal(newBT)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist."
    else:
        customQueue = queue.Queue()     
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            if root.value.data == node:
                dNode = getDeepestNodeBT(rootNode)
                root.value.data = dNode.data
                deleteDeepestNodeBT(rootNode, dNode)
                print("The node is successfully deleted.") 
                return

            if root.value.leftChild:
                customQueue.enQueue(root.value.leftChild)
            if root.value.rightChild:
                customQueue.enQueue(root.value.rightChild)
        print("Fail to delete")

# deleteNodeBT(newBT, 'Hott')
# levelOrderTraversal(newBT) 

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been su...deleted."

deleteBT(newBT)
levelOrderTraversal(newBT)

