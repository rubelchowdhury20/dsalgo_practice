################
# Leetcode 124 #
################

import math
class Solution:
    def maxPathSum(self, root):
        self.max_sum = -1000000000000
        self.traverseTree(root)
        return self.max_sum

    def traverseTree(self, node):
        if node is not None:
            left_sum, right_sum = 0, 0
            if node.left is not None:
                left_sum = self.traverseTree(node.left)
            if node.right is not None:
                right_sum = self.traverseTree(node.right)
            full_sum = left_sum + right_sum + node.val
            if full_sum > self.max_sum:
                self.max_sum = full_sum
            if left_sum > right_sum:
                current_sum = left_sum + node.val
                if current_sum > node.val:
                    if current_sum > self.max_sum:
                        self.max_sum = current_sum
                    return current_sum
                else:
                    if node.val > self.max_sum:
                        self.max_sum = node.val
                    return node.val
            else:
                current_sum = right_sum + node.val
                if current_sum > node.val:
                    if current_sum > self.max_sum:
                        self.max_sum = current_sum
                    return current_sum
                else:
                    if node.val > self.max_sum:
                        self.max_sum = node.val
                    return node.val
        return 0