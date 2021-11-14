# Created by Huimin on 11/8/2021


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    else:
        if nodeValue <= rootNode.data:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                insertNode(rootNode.rightChild, nodeValue)
    return "The node has been ...inserted."


def preOrderTraversal(rootNode):
    if not rootNode:  # termination condition
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


from BinaryTree import deleteNodeBT
import QueueLinkedList as queue


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue(
        )  # level order traversal resembles queue in FIFO way.
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enQueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enQueue(root.value.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found.")
    else:
        """ if nodeValue < rootNode.data:
                searchNode(rootNode.leftChild, nodeValue)
            else:
                searchNode(rootNode.rightChild, nodeValue) """
        if nodeValue < rootNode.data:
            if rootNode.leftChild is None:
                print("The value is not found.")
                return
            else:
                if rootNode.leftChild.data == nodeValue:
                    print("The value is found.")
                else:
                    searchNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                print("The value is not found.")
                return
            else:
                if rootNode.rightChild.data == nodeValue:
                    print("The value is found.")
                else:
                    searchNode(rootNode.rightChild, nodeValue)


def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(
            rootNode.leftChild,
            nodeValue)  # return rootNode as rootNode.leftChild
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        # base case
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = minValueNode(rootNode.rightChild)  # successor
        rootNode.data = temp.data  # substitute the node data with the successor data
        rootNode.rightChild = deleteNode(rootNode.rightChild,
                                         temp.data)  # delete the successor
    return rootNode


def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been su...deleted." """ """


newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))
print(minValueNode(newBST.rightChild))
deleteNode(newBST, 70)
levelOrderTraversal(newBST)
