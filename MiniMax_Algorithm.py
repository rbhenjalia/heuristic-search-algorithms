# -*- coding: utf-8 -*-
"""
@author:RAHUL BHENJALIA
@id : RB918555
"""

class Node:
    def __init__(self, left_node, right_node, next_type=None, value=None):

        if value is not None:
            self.value = value
            self.is_leaf = True
            self.next_type = next_type
            self.left = self.right = None
            self.direction = None
        else:
            self.is_leaf = False
            self.left = left_node
            self.right = right_node

        
            if left_node.next_type == 'min' and right_node.next_type == 'min':
                self.next_type = 'max'
                self.value = min(left_node.value, right_node.value)
            else:
                self.next_type = 'min'
                self.value = max(left_node.value, right_node.value)

          
            if self.value == left_node.value:
                self.direction = 'LEFT'
            else:
                self.direction = 'RIGHT'


class MiniMaxTree:
    def __init__(self, values):
        self.values = values

    def build(self):
        self.visited = 0
        left_index = 0
        right_index = len(self.values) - 1
        return self.__builderHelper(left_index, right_index, 0)

    def __builderHelper(self, left_index, right_index, d):
        if left_index == right_index:
            next_type = 'max'
            if d % 2 == 0:
                next_type = 'min'
            return Node(None, None, next_type, self.values[left_index])

        middle_index = (left_index + right_index) // 2
        return Node(
            self.__builderHelper(left_index, middle_index, d + 1),  # LEFT SUBTREE
            self.__builderHelper(middle_index + 1, right_index, d + 1)

        )

def get_path(node):
    result = []
    result_dir = []
    while True:
        if node.is_leaf:
            break
        result.append(node.value)
        result_dir.append(node.direction)
        if node.direction == 'LEFT':
            node = node.left
        else:
            node = node.right
    return result, result_dir


def getMiniMaxValueAndPath(tree):
    root_node = tree.build()
    return root_node.value, get_path(root_node)


# IMPLEMENTATION OF MINIMAX
print('---------------------------- MINMAX IMPLEMENTATION ------------------------------------')
Nodes = [3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1]
miniMax_tree = MiniMaxTree(Nodes)
root_value, path = getMiniMaxValueAndPath(miniMax_tree)
print('RESULT VALUE: ' + str(root_value))
print('\n')
print('PATH:')
is_first = False
for path_value in path[0]:
    if is_first:
        print(' ---> ', end='')
    else:
        is_first = True
    print(path_value, end='')
first = False
print('\n')
print("DIRECTION TAKEN:")
for path_direction in path[1]:
    if first:
        print(' ---> ', end='')
    else:
        first = True
    print(path_direction, end='')
    
print('\n')
print("INDEX OF THE RESULTED VALUE :  ",end='')
print(Nodes.index(path[0][0]))
print('---------------------------- -----------------------------------------------------------')
