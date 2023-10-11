################
# Leetcode 297 #
################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        print("serialize")
        if root is not None:
            serialized_array = [root.val]
            queue = [root]
        else:
            serialized_array = []
            queue = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left is not None:
                queue.append(current_node.left)
                serialized_array.append(current_node.left.val)
            else:
                serialized_array.append(None)
            if current_node.right is not None:
                queue.append(current_node.right)
                serialized_array.append(current_node.right.val)
            else:
                serialized_array.append(None)
        if root is not None:
            current_val = serialized_array[-1]
            while(current_val is None):
                serialized_array.pop()
                current_val = serialized_array[-1]
        return str(serialized_array)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print("deserialize")
        data = data.strip('][').strip()
        if len(data) > 0:
            data = [i.strip() for i in data.split(',')]
            data = [int(i) if i != 'None' else None  for i in data]
            root = TreeNode(data.pop(0))
            old_node_list = [root]
            current_node_list = []
            while(len(data)>0):
                print("hello")
                print(len(data))
                current_node = old_node_list.pop(0)
                if len(data)> 0:
                    left_node_val = data.pop(0)
                    if left_node_val is not None:
                        node = TreeNode(left_node_val)
                        current_node.left = node
                        current_node_list.append(node)
                if len(data)> 0:
                    right_node_val = data.pop(0)
                    if right_node_val is not None:
                        node = TreeNode(right_node_val)
                        current_node.right = node
                        current_node_list.append(node)
                if len(old_node_list) == 0:
                    old_node_list = current_node_list
                    current_node_list = []
            print("hello ji")
            return root
        else:
            return None




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))