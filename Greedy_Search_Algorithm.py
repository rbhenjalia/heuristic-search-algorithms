# -*- coding: utf-8 -*-
"""
@author: RAHUL BHENJALIA
@id : RB918555
"""

import heapq as hp


def greedy(start, goal, Graph, H):
    
    heap = []
    path = []
    heap_next = []
    heap_next2=[]
    hp.heapify(heap)
    hp.heapify(heap_next)
    hp.heapify(heap_next2)
    hp.heappush(heap, start)

    while heap:
        node = hp.heappop(heap)
        if node in path:
            continue
        path.append(node)
        for children in Graph[node]:
            if children == goal:
                return path + [children]
            else:
                for [node1, node2] in cost:
                    if node1 == node:
                        if node2 == children:
                            hp.heappush(heap_next, list((H[node2], node1, node2)))
        shortest = hp.heappop(heap_next)
        if node == shortest[1]:
            hp.heappush(heap, shortest[2])

        while heap:
            node = hp.heappop(heap)
            if node in path:
                continue
            path.append(node)
            for children in Graph[node]:
                if children == goal:
                    return path + [children]
                else:
                    for [node1, node2] in cost:
                        if node1 == node:
                            if node2 == children:
                                hp.heappush(heap_next, list((H[node2], node1, node2)))
            shortest = hp.heappop(heap_next)
            if node == shortest[1]:
                hp.heappush(heap, shortest[2])



Graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd', 'f'],
    'd': ['b', 'c', 'e', 's'],
    'e': ['d', 'h', 'r', 's'],
    'f': ['c', 'g', 'r'],
    'g': ['f'],
    'h': ['e', 'p', 'q'],
    'p': ['h', 'q', 's'],
    'q': ['h', 'p'],
    'r': ['e', 'f'],
    's': ['d', 'e', 'p']
}

cost = {
    ('a', 'b'): 2,
    ('a', 'c'): 2,
    ('b', 'd'): 1,
    ('d', 'c'): 8,
    ('d', 'e'): 2,
    ('s', 'd'): 3,
    ('s', 'e'): 9,
    ('s', 'p'): 1,
    ('p', 'h'): 4,
    ('p', 'q'): 15,
    ('q', 'h'): 4,
    ('h', 'e'): 8,
    ('c', 'f'): 3,
    ('e', 'r'): 2,
    ('r', 'f'): 2,
    ('f', 'g'): 2,
}

H = {
    'a': 5,
    'b': 7,
    'c': 4,
    'd': 7,
    'e': 5,
    'f': 2,
    'g': 0,
    'h': 11,
    'p': 14,
    'q': 12,
    'r': 3,
    's': 0
}

x = str(greedy('s', 'g', Graph, H))
print("Shortest Path Using Greedy Search: " + x)
