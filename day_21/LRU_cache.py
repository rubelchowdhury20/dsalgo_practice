################
# Leetcode 146 #
################

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.value_dict = {}
        self.node_dict = {}
        self.capacity = capacity
        self.count = 0
        self.head = Node()
        self.tail = self.head


    def vis_linkedlist(self):
        current_node = self.head
        node_list = []
        while current_node:
            node_list.append(str(current_node.val))
            current_node = current_node.next
        print("->".join(node_list))

    def update_linkedlist(self, key):
        node = self.node_dict[key]

        if node.prev is None:
            pass
        elif node.next is None:
            self.tail = node.prev
            node.prev.next = None
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None

        

    def get(self, key: int) -> int:
        if key in self.value_dict:
            self.update_linkedlist(key)
            # self.vis_linkedlist()
            return self.value_dict[key]
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.value_dict:
            self.value_dict[key] = value
            self.update_linkedlist(key)
        else:
            if self.count < self.capacity:
                self.value_dict[key] = value
                if self.head.val is None:
                    self.head.val = key
                    self.node_dict[key] = self.head
                else:
                    new_node = Node(key)
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                    self.node_dict[key] = self.head
                self.count += 1
            else:
                least_recent_key = self.tail.val
                self.tail.val = key
                del self.value_dict[least_recent_key]
                self.value_dict[key] = value
                self.node_dict[key] = self.node_dict.pop(least_recent_key)
                self.update_linkedlist(key)
        # print(self.value_dict)
                
                




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)