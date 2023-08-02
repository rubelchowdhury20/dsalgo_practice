################
# Leetcode 460 #
################

### Unsolved ###

class Node:
    def __init__(self, val=None, freq=0):
        self.val = val
        self.freq = freq
        self.next = None
        self.prev = None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.value_dict = {}
        self.node_dict = {}
        self.head = Node()
        self.tail = self.head
    
    def vis_llist(self):
        current_node = self.head
        val_list = []
        while(current_node is not None):
            val_list.append(str(current_node.val) + " " + str(current_node.freq))
            current_node = current_node.next
        print("->".join(val_list))

    
    def update_llist(self, key):
        print(key)
        node = self.node_dict[key]
        print(node.freq)
        print(self.head.val)
        print(self.head.freq)
        if node.prev is None:
            print(key)
            node.freq += 1
        elif node.next is None:
            node.freq += 1
            current_node = node
            while(current_node and current_node.freq <= node.freq):
                current_node = current_node.prev
            
            if current_node is None:
                print("......")
                print(self.head.val)
                print(self.tail.val)
                if self.head.next:
                    print(self.head.next.val)
                if node.prev:
                    print(node.prev.val)
                self.tail = node.prev
                self.tail.next = None
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.head.prev = None
                print(self.head.val)
                print(self.tail.val)
            else:
                if current_node.next != node:
                    self.tail = node.prev
                    self.tail.next = None
                    new_next = current_node.next
                    current_node.next = node
                    node.next = new_next
                    new_next.prev = node
                    node.prev = current_node
        else:
            node.freq += 1
            current_node = node
            while(current_node and current_node.freq <= node.freq):
                current_node = current_node.prev
            if current_node is None:
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.head.prev = None
            else:
                if current_node.next != node:
                    new_next = current_node.next
                    current_node.next = node
                    node.next = new_next
                    new_next.prev = node
                    node.prev = current_node


        

    def get(self, key: int) -> int:
        print("get operation started", key)
        if key in self.value_dict:
            self.update_llist(key)
            print(self.head.val)
            print(self.tail.val)
            # self.vis_llist()
            return self.value_dict[key]
        else:
            print("key not found")
            return -1
        

    def put(self, key: int, value: int) -> None:
        print("put operation started", key, value)
        print(self.tail.val)
        if key in self.value_dict:
            self.value_dict[key] = value
            self.update_llist(key)
        else:
            if self.count < self.capacity:
                self.value_dict[key] = value
                if self.count == 0:
                    self.head.val = key
                    self.head.freq += 1
                    self.node_dict[key] = self.head
                else:
                    new_node = Node(val=key)
                    self.node_dict[key] = new_node
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = self.tail.next
                    self.tail.next = None
                    self.node_dict[key] = self.tail
                    self.update_llist(key)
                self.count += 1
            else:
                least_frequent_key = self.tail.val
                self.tail.val = key
                self.tail.freq = 0
                del self.value_dict[least_frequent_key]
                self.value_dict[key] = value
                self.node_dict[key] = self.node_dict.pop(least_frequent_key)
                self.update_llist(key)
        # self.vis_llist()
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)