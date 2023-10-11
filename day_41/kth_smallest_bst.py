################
# Leetcode 230 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_list = self.traverseTree(root)
        return node_list[k-1]
        

    def traverseTree(self, node):
        node_list = []
        if node is not None:
            left_nodes = self.traverseTree(node.left)
            right_nodes = self.traverseTree(node.right)
            node_list.extend(left_nodes)
            node_list.append(node.val)
            node_list.extend(right_nodes)
        return node_list