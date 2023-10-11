################
# Leetcode 653 #
################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = [root]
        while(len(queue) > 0):
            current_node = queue.pop(0)
            remaining = k - current_node.val
            if remaining != current_node.val:
                if self.isKey(root, remaining):
                    return True
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
                
        return False


    def isKey(self, root, key):
        if root is not None:
            if root.val == key:
                return True
            elif root.val > key:
                return self.isKey(root.left, key)
            else:
                return self.isKey(root.right, key)
        return False
