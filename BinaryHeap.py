# Created by Huimin on 11/10/2021

from typing import NewType

from BinaryTree import deleteBT


class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0  # filled cells no./index of heap cells, 0 is ignored.
        self.maxSize = size + 1


def peekOfHeap(rootNode):
    if not rootNode:
        return None
    return rootNode.customList[1]


def sizeOfHeap(rootNode):
    if not rootNode:
        return None
    return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return None
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The b h is full."
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "SUCCESS"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = 2 * index
    rightIndex = 2 * index + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:  # no children
        return
    elif rootNode.heapSize == leftIndex:  # one child, basic condition
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        elif heapType == "Max":
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:  # two children
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp

        elif heapType == "Max":
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    extractedNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractedNode


def deleteEntireBP(rootNode):
    rootNode.customList = None


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
deleteEntireBP(newBinaryHeap)
levelOrderTraversal(newBinaryHeap)