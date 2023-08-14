################
# Leetcode 103 #
################

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level_dict = {}
        self.levelRecursion(root)
        level_list = []
        for key in self.level_dict:
            if key % 2 == 0:
                level_list.append(self.level_dict[key])
            else:
                level_list.append(self.level_dict[key][::-1])
            self.level_dict[key] = None
        return level_list

        

    def levelRecursion(self, root, count=0):
        if root is not None:
            if count in self.level_dict:
                self.level_dict[count].append(root.val)
            else:
                self.level_dict[count] = [root.val]
            count += 1
            if root.left is not None:
                self.levelRecursion(root.left, count)
            if root.right is not None:
                self.levelRecursion(root.right, count)