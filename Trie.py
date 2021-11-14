# Created by Huimin on 11/10/2021


class TrieNode:
    def __init__(self):
        self.children = {}  # store both data and links to children
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)  # link to children node
            if node == None:
                node = TrieNode()
                current.children.update({char:
                                         node})  # char and link to blank node
            current = node
        current.endOfString = True
        print("success..inserted")

    def searchString(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)  # link to children node
            if node == None:
                return False
            current = node
        return current.endOfString


def deleteString(root, word, index):
    char = word[index]
    currentNode = root.children.get(char)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:  #case 1, root is shared, can't delete
        deleteString(currentNode, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(
                currentNode.children
        ) >= 1:  # case 2: end flag of string coexists with other string char
            currentNode.endOfString = False
            return False
        else:  # end of string independently exits.
            root.children.pop(
                char
            )  # WE POP the char-link pair, but node delete the node completely, b/c we may have property
            return True

    if currentNode.endOfString == True:  #????repeat function code?
        deleteString(currentNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
    if canThisNodeBeDeleted:
        root.Children.pop(char)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("App"))
print(deleteString(newTrie.root, "App", 0))
print(newTrie.searchString("App"))
# newTrie.insertString("PP")
# print(newTrie.searchString("PP"))
