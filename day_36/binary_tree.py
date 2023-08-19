import random

class Node():
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insertion(self, key):
        y = None
        x = self.root
        while(x is not None):
            y = x
            if key>x.key:
                x = x.right
            else:
                x = x.left
        z_node = Node(key)
        z_node.p = y
        if self.root is None:
            self.root = z_node
        elif key > y.key:
            y.right = z_node
        else:
            y.left = z_node
        

    def search_key(self, node, key):
        if node is None or node.key == key:
            return node
        if key > node.key:
            return self.search_key(node.right, key)
        else:
            return self.search_key(node.left, key)
        
    def levelOrder(self, node):
        self.level_dict = {}
        self.levelRecursion(node)
        return self.level_dict
    
    def levelRecursion(self, node, count=0):

        if node is not None:
            if count in self.level_dict:
                self.level_dict[count].append(node.key)
            else:
                self.level_dict[count] = [node.key]
            count += 1
            if node.left is not None:
                self.levelRecursion(node.left, count)
            if node.right is not None:
                self.levelRecursion(node.right, count)



    def inorder_traverse(self, node):
        if node is not None:
            print(node.key)
            self.inorder_traverse(node.left)
            self.inorder_traverse(node.right)

    def get_root(self):
        return self.root
    
    def find_minimum(self, node):
        while(node.left is not None):
            node = node.left
        return node
    
    def find_maximum(self, node):
        while(node.right is not None):
            node = node.right
        return node
    
    def find_successor(self, node):
        if node.right is not None:
            return self.find_minimum(node.right)
        node_p = node.p
        while(node_p is not None and node_p.right == node):
            node = node_p
            node_p = node.p
        return node_p
    
    def find_predecessor(self, node):
        if node.left is not None:
            return self.find_maximum(node.left)
        
        node_p = node.p
        while(node_p is not None and node_p.left == node):
            node = node_p
            node_p = node.p
        return node_p 
    
    def remove_node(self, node):
        if node.left is None:
            if node.right is None:
                if node.p is not None:
                    if node.p.left is not None and node.p.left == node:
                        node.p.left = None
                    else:
                        node.p.right = None
                else:
                    node = None
            else:
                if node.p is not None:
                    if node.p.left is not None and node.p.left == node:
                        node.p.left = node.right
                        node.right.p = node.p
                    else:
                        node.p.right = node.right
                        node.right.p = node.p
                else:
                    node.right.p = None
                    self.root = node.right
                    
        else:
            if node.right is None:
                if node.p is not None:
                    if node.p.left is not None and node.p.left == node:
                        node.p.left = node.left
                        node.left.p = node.p
                    else:
                        node.p.right = node.left
                        node.left.p = node.p
                else:
                    node.left.p = None
                    self.root = node.left
            else:
                successor = self.find_successor(node)
                successor_p = successor.p
                if successor_p == node:
                    if node.p is not None:
                        if node.p.left is not None and node.p.left == node:
                            node.p.left = successor
                        else:
                            node.p.rigth = successor
                        successor.p = node.p
                        successor.left = node.left
                        successor.left.p = successor
                    else:
                        self.root = successor
                        successor.left = node.left
                        successor.left.p = successor
                else:
                    node_right = node.right
                    node_left = node.left
                    if successor_p.left is not None and successor_p.left == successor:
                        successor_p.left = None
                    else:
                        successor_p.right = None
                    node_p = node.p
                    if node_p is not None:
                        successor_p = node_p
                        if node_p.left is not None and node.p.left == node:
                            node_p.left = successor
                        else:
                            node_p.right = successor  
                    else:
                        successor.p = None                  
                    successor.left = node_left
                    node_left.p = successor
                    successor.right = node_right
                    node_right.p = successor



bt = BinaryTree()
nums = []
for i in range(10):
    num = random.randint(1, 100)
    nums.append(num)
    bt.insertion(num)
# nums = [93, 19, 18, 13, 58, 10, 32, 15, 8, 84]
# for i in nums:
#     bt.insertion(i)
print(nums)
print("...........")
root_node = bt.get_root()
# bt.inorder_traverse(root_node)
print("level traversing outputs")
print(bt.levelOrder(root_node))
print("search functionality")
print(nums[5])
print(bt.search_key(root_node, nums[5]).key)
print("Minimum and maximum elements are {} and {}".format(bt.find_minimum(root_node).key, bt.find_maximum(root_node).key))
successor_element = bt.find_successor(bt.search_key(root_node, nums[5]))
if successor_element is not None:
    print("succesor element of {} is {}".format(bt.search_key(root_node, nums[5]).key, successor_element.key))
    bt.remove_node(successor_element)
else:
    print("successor element is none")
# print("predecessor element of {} is {}".format(bt.search_key(root_node, nums[5]).key, bt.find_predecessor(bt.search_key(root_node, nums[5])).key))
successor_element = bt.find_successor(bt.search_key(root_node, nums[5]))
if successor_element is not None:
    print("succesor element of {} after one removal is {}".format(bt.search_key(root_node, nums[5]).key, successor_element.key))
else:
    print("successor element is none")
print(bt.levelOrder(bt.get_root()))
