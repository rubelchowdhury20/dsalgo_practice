################
# Leetcode 427 #
################

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 1:
            current_node = Node(grid[0][0], True, None, None, None, None)
        else:
            mid_y = len(grid)//2
            mid_x = len(grid[0])//2

            topLeft_grid = [i[:mid_x] for i in grid[:mid_y]]
            topRight_grid = [i[mid_x:] for i in grid[:mid_y]]
            bottomLeft_grid = [i[:mid_x] for i in grid[mid_y:]]
            bottomRight_grid = [i[mid_x:] for i in grid[mid_y:]]

            topLeft = self.construct(topLeft_grid)
            topRight = self.construct(topRight_grid)
            bottomLeft = self.construct(bottomLeft_grid)
            bottomRight = self.construct(bottomRight_grid)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                if (topLeft.val and topRight.val and bottomLeft.val and bottomRight.val) or (not topLeft.val and not topRight.val and not bottomLeft.val and not bottomRight.val):
                    current_node = Node(topLeft.val, True, None, None, None, None)
                else:
                    current_node = Node(topLeft.val, False, topLeft, topRight, bottomLeft, bottomRight)
            else:
                current_node = Node(topLeft.val, False, topLeft, topRight, bottomLeft, bottomRight)
        return current_node