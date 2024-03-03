class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next



class DLL:
    def __init__(self):
        self.tail = Node()
        self.head = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        return_str = ""
        curr_head = self.head.next
        while curr_head != self.tail:
            return_str += f"{curr_head.data} "
            curr_head = curr_head.next
        return return_str

    def push_front(self, data):
        new_node = Node(data)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node


    def push_back(self, data):
        new_node = Node(data)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node

        self.tail.prev = new_node
        # self.tail.prev.next = new_node


    def remove_front(self):
        if self.head.next != self.tail:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head


    def remove_back(self):
        if self.head.next != self.tail:

            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail

    def get_first(self):
        return self.head.next.data

    def get_last(self):
        return self.tail.prev.data
    
    def print_reverse(self):
        return_str = ""
        curr_head = self.tail.prev
        while curr_head != self.head:
            return_str += f"{curr_head.data} "
            curr_head = curr_head.prev
        print(return_str)


    def get_size(self):
        size = 0
        curr_head = self.head.next
        while curr_head != self.tail:
            size += 1
            curr_head = curr_head.next
        return size

# x = DLL()
# x.push_front(4)
# print(x)
# x.push_back(5)
# print(x)
# x.push_front(10)
# print(x)
# x.push_back(1)
# print(x)
# x.remove_back()
# print(x)
# size = x.get_size()
# print(size)
# x.push_front(4)
# print(x)
# size = x.get_size()
# print(size)
# x.push_front(4)
# size = x.get_size()
# print(size)
# print(x)



class DLL_PosList:
    def __init__(self):
        self.tail = Node()
        self.head = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current_node = self.tail

    def insert(self, value):
        prev = self.current_node.prev
        next = self.current_node
        new_node = Node(value)
        new_node.next = next
        new_node.prev = prev
        prev.next = new_node
        next.prev = new_node
      
        self.current_node = new_node

    def __str__(self):
        return_str = ""
        curr_head = self.head.next
        while curr_head != self.tail:
            return_str += f"{curr_head.data} "
            curr_head = curr_head.next
        return return_str


x = DLL_PosList()
print(x)
x.insert("A")
print(x)
x.insert("B")
print(x)
x.insert("C")
print(x)




