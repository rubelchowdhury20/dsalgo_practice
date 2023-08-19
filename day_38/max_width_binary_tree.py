################
# Leetcode 662 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.node_map = {}
        self.inorderTraverse(root, 0, 0)
        max_ = 0
        for i in self.node_map:
            if self.node_map[i]["max"] - self.node_map[i]["min"] + 1 > max_:
                max_ = self.node_map[i]["max"] - self.node_map[i]["min"] + 1
        return max_
        
        

    def inorderTraverse(self, node, pos_x, pos_y):
        if node is not None:
            if pos_y in self.node_map:
                if pos_x < self.node_map[pos_y]["min"]:
                    self.node_map[pos_y]["min"] = pos_x
                if pos_x > self.node_map[pos_y]["max"]:
                    self.node_map[pos_y]["max"] = pos_x
            else:
                self.node_map[pos_y] = {}
                self.node_map[pos_y]["min"] = pos_x
                self.node_map[pos_y]["max"] = pos_x
            self.inorderTraverse(node.left, 2*pos_x, pos_y+1)
            self.inorderTraverse(node.right,2*pos_x+1, pos_y+1)
        