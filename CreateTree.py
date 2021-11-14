# Created by Huimin on 11/7/2021

class TreeNode:
    def __init__(self, data, children=[]): # by default the node is a leaf(that has no children)
        self.data = data
        self.children = children

    def __str__(self, level = 0): # print out the current tree
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
print(tree)
cold = TreeNode('Cold', [])
print(cold)
hot = TreeNode('Hot', [])
print(hot)
tree.addChild(cold)
print(tree)
tree.addChild(hot)
print(tree)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
hot.addChild(tea)
hot.addChild(coffee)
print(tree)
