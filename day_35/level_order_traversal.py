################
# Leetcode 102 #
################

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         return self.levelRecursion(root)

#     def levelRecursion(self, root, count=0):
#         if count == 0 and root is not None:
#             root_list = [[root.val]]
#         else:
#             root_list = []
#         count += 1
#         if root is not None:
#             level_list = []
#             inner_left_nodes = []
#             inner_right_nodes = []
#             if root.left is not None:
#                 level_list.append(root.left.val)
#                 inner_left_nodes = self.levelRecursion(root.left, count)
#             if root.right is not None:
#                 level_list.append(root.right.val)
#                 inner_right_nodes = self.levelRecursion(root.right, count)
#             merged_nodes = []
#             if len(inner_right_nodes)>len(inner_left_nodes):
#                 for idx, i in enumerate(inner_left_nodes):
#                     i.extend(inner_right_nodes[idx])
#                     merged_nodes.append(i)
#                 merged_nodes.extend(inner_right_nodes[len(inner_left_nodes):])
#             else:
#                 for idx, i in enumerate(inner_right_nodes):
#                     inner_left_nodes[idx].extend(i)
#                     merged_nodes.append(inner_left_nodes[idx])
#                 merged_nodes.extend(inner_left_nodes[len(inner_right_nodes):])
#             if len(level_list) > 0:
#                 root_list.append(level_list)
#             root_list.extend(merged_nodes)
#             # if len(inner_left_nodes)>0:
#             #     root_list.extend(inner_left_nodes)
#             # if len(inner_right_nodes)>0:
#             #     root_list.extend(inner_right_nodes)
#         return root_list



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level_dict = {}
        self.levelRecursion(root)
        level_list = []
        for key in self.level_dict:
            level_list.append(self.level_dict[key])
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

  

