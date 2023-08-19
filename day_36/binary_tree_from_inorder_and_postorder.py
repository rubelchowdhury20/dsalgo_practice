################
# Leetcode 105 #
################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.indorder = inorder
        self.preorder_dict = {}
        for i, idx in enumerate(preorder):
            self.preorder_dict[idx] = i
        return self.treeFormation(inorder)
        
        # inorder_dict = {}
        # for i, idx in enumerate(inorder):
        #     inorder_dict[idx] = i


    def treeFormation(self, array):
        min_ = self.preorder_dict[array[0]]
        min_idx = 0
        for idx, i in enumerate(array):
            if self.preorder_dict[i]<min_:
                min_ = self.preorder_dict[i]
                min_idx = idx
        node = TreeNode(array[min_idx])
        if min_idx > 0:
            left_child_node = self.treeFormation(array[:min_idx])
            node.left = left_child_node
        if min_idx < len(array)-1:
            right_child_node = self.treeFormation(array[min_idx+1:])
            node.right = right_child_node
        return node
        
        