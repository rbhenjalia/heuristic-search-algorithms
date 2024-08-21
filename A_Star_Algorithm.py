# -*- coding: utf-8 -*-
"""
@author:RAHUL BHENJALIA
@id : RB918555
"""

import heapq
from collections import defaultdict


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def isEmpty(self):
        return len(self._queue) == 0

    def getSize(self):
        return self._index


class Node:

    def __init__(self, value, costs):
        self.value = value
        self.costs = costs

    def Value(self):
        return self.value

    def getCost(self):
        return self.costs


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.path = []
        self.state=[]
        self.next = defaultdict(list)

    def add(self, start, goal, G):
        self.nodes[start], self.nodes[goal] = start, goal
        edge = (start, goal, G)
        self.edges.append(edge)
        self.next[start.Value()].append((goal, G))

    def getPath(self):
        return self.path

    def getState(self):
        return self.state

    def paths(self, start, end):
        G, H = 0, start.getCost()
        queue = PriorityQueue()
        cost, list = {}, {}
        cost[start.Value()] = 0
        for node in self.nodes:
            cost[node.Value()] = 0
            list[node.Value()] = 0
        F = G + H
        queue.insert((start, G, H), F)
        while not False:
            total = 0
            cur, G, H = queue.remove()
            next = self.next[cur.Value()]

            for nextNode in next:
                goal, G = nextNode
                totalG = G + G
                H = goal.getCost()
                F = totalG + H
                queue.insert((goal, totalG, H), F)

                if queue.isEmpty():

                    while curr_node:
                        self.state.append(curr_node)
                        curr_node = list[curr_node]
                    self.state = self.state[::-1]

                if cost[goal.Value()]:
                    if cost[goal.Value()] > totalG:   # CHECK IF THERE IS A SHORTER PATH
                        cost[goal.Value()] = totalG   # SET THAT PATH
                        list[goal.Value()] = cur.Value()
                else:
                    cost[goal.Value()] = totalG  #OTHERWISE SET IT TO THE SAME
                    list[goal.Value()] = cur.Value()

            if queue.isEmpty():
                curr_node = end.Value()
                while curr_node:
                    self.path.append(curr_node)
                    self.state.append(curr_node)
                    curr_node = list[curr_node]
                self.path = self.path[::-1]
                self.state = self.state[::-1]

                return total

         

#-------------------Assigning Heuristic Values----------------#
s = Node('s', 0)
a = Node('a', 5)
b = Node('b', 7)
c = Node('c', 4)
d = Node('d', 7)
e = Node('e', 5)
f = Node('f', 2)
h = Node('g', 11)
p = Node('p', 14)
r = Node('r', 3)
q = Node('q', 12)
g = Node('g', 0)

Graph = Graph()

#-------------------Adding the Graph --------------------------#

Graph.add(s, d, 3)
Graph.add(s, p, 1)
Graph.add(s, e, 9)
Graph.add(a, b, 2)
Graph.add(a, c, 2)
Graph.add(b, d, 1)
Graph.add(c, d, 8)
Graph.add(d, e, 2)
Graph.add(e, h, 8)
Graph.add(e, r, 2)
Graph.add(r, f, 2)
Graph.add(f, g, 2)
Graph.add(p, q, 15)
Graph.add(p, h, 4)
Graph.add(q, h, 4)

Graph.paths(s, g)
path = Graph.getPath()
state = Graph.getState()

print('------------------ A* Algorithm -----------------------------')
print(' Path With The Lowest Cost' + " : " + str(path))
print(' States Expanded' + " : " + str(state))
print('-------------------------------------------------------------')
