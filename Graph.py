# Created by Huimin on 11/12/2021


class Graph:  # represent graph(node, edge) in python
    def __init__(self, gdict=None):
        if gdict == None:
            self.gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


customeDict = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['e', 'b', 'f'],
    'e': ['d', 'f'],
    'f': ['d', 'e']
}

graph = Graph()
print(graph.gdict)