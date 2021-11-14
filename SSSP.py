# Created by Huimin on 11/12/2021


class Graph:  # represent graph(node, edge) in python
    def __init__(self, gdict=None):
        if gdict == None:
            self.gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append([start])
