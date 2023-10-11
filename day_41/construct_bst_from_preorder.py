#################
# Leetcode 1008 #
#################

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        node = TreeNode(preorder[0])
        left_values = []
        right_values = []
        x = preorder[0]
        for i in preorder[1:]:
            if i < x:
                left_values.append(i)
            elif i > x:
                right_values.append(i)
        # left_values = [i for i in preorder[1:] if i < preorder[0]]
        # right_values = [i for i in preorder[1:] if i > preorder[0]]
        if len(left_values) > 0:
            node.left = self.bstFromPreorder(left_values)
        if len(right_values) > 0:
            node.right = self.bstFromPreorder(right_values)
        return node
