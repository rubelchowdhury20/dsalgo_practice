class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, node_values):
        self.head = None
        if len(node_values) > 0:
            self.head = Node(node_values[0])
            current_node = self.head
            for i in node_values[1:]:
                new_node = Node(i)
                current_node.next = new_node
                current_node = new_node

    def __repr__(self):
        current_node = self.head
        node_values = []
        while(current_node.next is not None):
            node_values.append(current_node.value)
            current_node = current_node.next
        node_values.append(current_node.value)
        return "->".join(node_values)

    def __iter__(self):
        current_node = self.head
        while(current_node.next is not None):
            yield current_node
            current_node = current_node.next
        yield current_node

    def check(self):
        for i in self:
            print(i.value)

    def reverse(self):
        prev_node_next = None
        count = 0
        for i in self:
            if count>0:
                prev_node.next = prev_node_next
                prev_node_next = prev_node
            prev_node = i
            count += 1
        prev_node.next = prev_node_next
        self.head = prev_node

    def return_middle_value(self):
        count = 0
        for i in self:
            count += 1
        m = count//2
        count = 0
        for i in self:
            if count == m:
                return i.value
            count += 1

    def remove_given_node(self, n):
        if self.head is None:
            raise Exception("no nodes present")
        elif n == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            for i in self:
                if count == n:
                    prev_node.next = i.next
                    return
                prev_node = i
                count += 1
        raise Exception("The entered index is out of limit")



llist = LinkedList(["ram", "shyam", "jadu", "madhu", "aaron", "venki"])
llist.reverse()
llist.check()
print("the middle value is ", llist.return_middle_value())
llist.remove_given_node(2)
print(llist)
        
