################
# Leetcode 705 #
################

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None

class MyHashSet:

    def __init__(self):
        self.key_space = 2003
        self.hash_table = [Node() for i in range(self.key_space)]

    def get_hash_value(self, key):
        return hash(key) % self.key_space
        

    def add(self, key: int) -> None:
        print("add called")
        hash_key = self.get_hash_value(key)
        key_found = False
        current_node = self.hash_table[hash_key]
        if current_node.key is None:
            current_node.key = key
        else:
            while(current_node.next and not key_found):
                if current_node.key == key:
                    key_found = True
                current_node = current_node.next

        if key_found:
            print("key already exists")
        else:
            if current_node.key == key:
                print("key already exists")
            else:
                current_node.next = Node(key)
                current_node.next.prev = current_node

    def remove(self, key: int) -> None:
        print("remove called")
        hash_key = self.get_hash_value(key)
        key_found = False
        current_node = self.hash_table[hash_key]
        if current_node.key == key:
            current_node.key = None
            return key
        else:
            while(current_node.next and not key_found):
                if current_node.key == key:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    return key
                current_node = current_node.next
        if not key_found:
            if current_node.key == key:
                current_node.prev.next = None
                return key
        

    def contains(self, key: int) -> bool:
        print("contain called")
        hash_key = self.get_hash_value(key)
        key_found = False
        current_node = self.hash_table[hash_key]
        while(current_node and not key_found):
            if current_node.key == key:
                key_found = True
            current_node = current_node.next
        if key_found:
            return True
        else:
            return False