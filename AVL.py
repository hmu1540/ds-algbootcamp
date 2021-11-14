# Created by Huimin on 11/9/2021


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = getHeight(disbalancedNode)
    newRoot.height = getHeight(newRoot)
    # disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    # newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = getHeight(disbalancedNode)
    newRoot.height = getHeight(newRoot)
    return newRoot


""" def getBalance(rootNode):
    return abs(getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)) <= 1 """


def getBalance(rootNode):
    if not rootNode:
        return 0
    else:
        return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        rootNode = AVLNode(nodeValue)
    else:
        if nodeValue <= rootNode.data:
            rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
        if nodeValue > rootNode.data:
            rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild),
                              getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue <= rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue <= rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


def getMinValueNode(rootNode):
    """ current = rootNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current """
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)


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
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = getMinValueNode(rootNode.rightChild)  # successor
        rootNode.data = temp.data  # substitute the node data with the successor data
        rootNode.rightChild = deleteNode(rootNode.rightChild,
                                         temp.data)  # delete the successor
    rootNode.height = 1 + max(getHeight(rootNode.leftChild),
                              getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL tree has been su...deleted." """ """


newAVL = AVLNode(5)

newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
deleteAVL(newAVL)
levelOrderTraversal(newAVL)