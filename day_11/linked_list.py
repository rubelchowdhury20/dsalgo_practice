class Node():
    def __init__(self, value):
        self.value = value
        self.next = None



# initializing a linkedlist with list of values

class LinkedList():
    def __init__(self, node_values):
        self.head = None
        if len(node_values) > 0:
            node = Node(node_values[0])
            self.head = node
            current_node = self.head
            for val in node_values[1:]:
                node = Node(val)
                current_node.next = node
                current_node = node

        

    def __repr__(self):
        node_values = []
        current_node = self.head
        while(current_node != None):
            node_values.append(current_node.value)
            current_node = current_node.next
        return ".".join(node_values)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def add_after(self, new_node, node_after):
        if self.head == None:
            raise Exception("Empty nodes")
        elif self.head.next == None:
            self.head.next = new_node
            return
        else:
            for i in self:
                print(i.value, node_after)
                if i.value == node_after:
                    flag = i.next
                    i.next = new_node
                    new_node.next = flag
                    return
                    
        raise Exception("Node with value {} not found".format(node_after))

    def add_before(self, new_node, node_before):
        if self.head is None:
            raise Exception("node is empty")
        elif self.head.value == node_before:
            flag = self.head
            self.head = new_node
            self.head.next = flag
            return
        else:
            for i in self:
                if i.next is not None and i.next.value == node_before:
                    flag = i.next
                    i.next = new_node
                    new_node.next = flag
                    return
        raise Exception("The node with given value of {} is not found".format(node_before))

    def remove(self, target_node):
        if self.head is None:
            raise Exception("No node exists only!")
        elif self.head.value == target_node:
            self.head = None
            return
        else:
            # prev_node = self.head
            for i in self:
                if i.next.value == target_node:
                    i.next = i.next.next
                    return
        raise Exception("given node with name {} was not found".format(target_node))

    def check_iteration(self):
        for i in self:
            print(i)

    

llist = LinkedList(["aaron", "Byron", "Cyclon"])
print(llist)
for i in llist:
    print(i.value)

new_node = Node("O_omega")
llist.add_first(new_node)
print(llist)

new_last_node = Node("deysey")
llist.add_last(new_last_node)
print(llist)

llist.check_iteration()

new_node = Node("mystery")
llist.add_after(new_node, "O_omega")
print(llist)

new_node = Node("begineuvor")
llist.add_before(new_node, "deysey")
print(llist)

llist.remove("deysey")
print(llist)
llist.remove("mystery")
print(llist)


