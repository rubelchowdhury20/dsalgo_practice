################
# Leetcode 108 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums)//2
        mid_node = TreeNode(nums[mid])
        if mid > 0:
            left_node = self.sortedArrayToBST(nums[:mid])
            mid_node.left = left_node
        if mid < len(nums) - 1:
            right_node = self.sortedArrayToBST(nums[mid+1:])
            mid_node.right = right_node
        return mid_node