# -*- coding: utf-8 -*-
"""
@author:RAHUL BHENJALIA
@id : RB918555
"""

from math import inf
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

class MiniMaxTree:
    def __init__(self, values):
        self.values = values

    def getResultWithPruning(self):
        self.visited = 0
        return self.__getResultWithAlphaBetaPruning(0, len(self.values) - 1, 0)

    def __getResultWithAlphaBetaPruning(self, left_index, right_index, d, alpha=-inf, beta=inf):
        self.visited += 1
        if left_index == right_index:
            if d % 2 == 0:
                alpha, beta = self.values[left_index], inf
            else:
                alpha, beta = -inf, self.values[right_index]
            return alpha, beta

        middle_index = (left_index + right_index) // 2
        
        # LEFT SUBTREE
        alpha_left, beta_left = self.__getResultWithAlphaBetaPruning(left_index, middle_index, d + 1, alpha, beta)
        if d % 2 == 0:
            alpha = beta_left
        else:
            beta = alpha_left
        if beta <= alpha:
            if d == 0:
                return alpha
            else:
                return alpha, beta
            
        # RIGHT SUBTREE
        
        alpha_right, beta_right = self.__getResultWithAlphaBetaPruning(middle_index + 1, right_index, d + 1, alpha,
                                                                       beta)
        if d % 2 == 0:
            alpha = max(alpha, beta_right)
        else:
            beta = min(beta, alpha_right)
        if d == 0:
            return alpha
        else:
            return alpha, beta


Nodes = [3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1]
miniMax_tree = MiniMaxTree(Nodes)
terminal_value = miniMax_tree.getResultWithPruning()

print('----------------- ALPHA-BETA PRUNING OF MINMAX TREE --------------------------')
print('RESULT VALUE: ' + str(terminal_value))
print('TOTAL VISITED VERTICES: ' + str(miniMax_tree.visited))
print('INDEX OF THE RESULTED VALUE: ' + str(Nodes.index(terminal_value)))
print('-----------------------------------------------------------------------------')