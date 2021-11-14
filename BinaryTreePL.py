# Created by Huimin on 11/8/2021

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The BT is full."
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been ...inserted."

    def searchNode(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Success"
        return "Not found"

    def preOrderTraversal(self, index): # traverse at index <index>
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
    
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1): # b/c python list to store nodes in the same order as level traversal, thus simgply print out the list elment 
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "The BT doesn't exist."
        else:
            """ deepestNode = self.customList[self.lastUsedIndex]
            self.customList[self.customList.index(value)] = deepestNode
            self.customList[self.lastUsedIndex] = None
            self.lastUsedIndex += 1  """ 
            for i in range(1, self.lastUsedIndex+1):
                if self.customList[i] == value:
                    self.customList[i] = self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    return "The value has been succ...deleted."
            return "The value does not exist."
    def deleteBT(self):
        self.customList = None
        return "The BT has been..."            

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

print(newBT.deleteBT())
