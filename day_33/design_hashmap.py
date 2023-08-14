################
# Leetcode 706 #
################


class Node:
    def __init__(self, key=None):
        self.key = key
        self.val = None
        self.next = None
        self.prev = None

class MyHashMap:

    def __init__(self):
        self.key_space = 2003
        self.hash_table = [Node() for i in range(self.key_space)]

    def get_hash_value(self, key):
        return hash(key) % self.key_space
        
    def put(self, key: int, value: int) -> None:
        hash_key = self.get_hash_value(key)
        current_node = self.hash_table[hash_key]
        hash_found = False
        if current_node.key is None:
            current_node.key = key
            current_node.val = value
        else:
            while(current_node.next and not hash_found):
                if current_node.key == key:
                    hash_found = True
                    current_node.val = value
                current_node = current_node.next
            if current_node.key == key:
                hash_found = True
                current_node.val = value
            else:
                current_node.next = Node(key)
                current_node.next.val = value
                current_node.next.prev = current_node


        
    def get(self, key: int) -> int:
        hash_key = self.get_hash_value(key)
        current_node = self.hash_table[hash_key]
        hash_found = False
        while(current_node.next is not None):
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next
        if current_node.key == key:
            return current_node.val
        return -1
        

    def remove(self, key: int) -> None:
        hash_key = self.get_hash_value(key)
        current_node = self.hash_table[hash_key]
        hash_found = False
        if current_node.key is None:
            return
        elif current_node.next is None:
            if current_node.key == key:
                current_node.key = None
                current_node.val = None
        else:
            if current_node.key == key:
                current_node.next.prev = None
                self.hash_table[hash_key] = current_node.next
            else:
                while(current_node.next and not hash_found):
                    if current_node.key == key:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                        hash_found = True
                    current_node = current_node.next
                if current_node.key == key:
                    current_node.prev.next = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



