from node2 import Node

def add(head_node, data):
    new_node = Node(data, head_node)
    return new_node

def string_func(head_node):
    if head_node == None:
        return ""
    ret_string = ""
    while head_node != None:
        ret_string += str(head_node.data) + ", "
        head_node = head_node.next
    ret_string = ret_string.strip(", ")
    return ret_string


# my_node = Node(12)
# my_node = add(my_node, 42)
# my_node = add(my_node, 100)
# my_node = add(my_node, 10)
# my_node = add(my_node, 50)
# print(my_node)
# print(string_func(my_node))

#recursively
def length(head_node):
    if head_node == None:
        return 0
    else:
        return 1 + length(head_node.next)
    
#iteratively
def length_iter(head_node):
    counter = 0
    curr_head = head_node
    while curr_head != None:
        counter += 1
        curr_head = curr_head.next
    return counter


def sum_of_values(head_node):
    result = 0
    curr_head = head_node
    while curr_head != None:
        result += curr_head.data
        curr_head = curr_head.next
    return result

#The list is already ordered
def add_correct_location(head, data):
    curr_node = head
    if head == None:
        n = Node(data)
        return n
    elif head.data < data:
            curr_node = Node(data)
            curr_node.next = head
            head = curr_node
            return head
    else:
        while curr_node.next != None:
            if curr_node.next.data < data:
                n = Node(data)
                n.next = curr_node.next
                curr_node.next = n
                return head
            curr_node = curr_node.next
        if curr_node.next == None:
            n = Node(data)
            curr_node.next = n
            return head



def reverse_order(head):
    if head == None:
        return head
    elif head.next == None:
        return head
    else:
        node = reverse_order(head.next)
        # if head.next.next == head:
        #     head.next.next = None
        # else:
        head.next.next = head
        head.next = None
        return node
        # head.next = None
        # return head
   
        
def merge_sort(head1, head2):
    pass
    



# print(length(my_node))
# print(length_iter(my_node))
# print(length(None))
# print(sum_of_values(my_node))
# my_node = add_correct_location(None,200)
# print(my_node)
# print(string_func(my_node))
# my_node = reverse_order(my_node)
# print(string_func(my_node))


class LinkedList:
    def __init__(self,head = None, tail = None):
        self.head = head
        self.tail = tail


    def push_front(self,data):
        if self.head == None:
            n = Node(data)
            n.next = self.head
            self.head = n
            self.tail = n
        else:
            n = Node(data)
            n.next = self.head
            self.head = n
      


    def pop_front(self):
        ret_value = self.head
        self.head = self.head.next
        return ret_value



    def push_back(self, data):
        n = Node(data)
        self.tail.next = n
        self.tail = n



    def pop_back(self):
        ret_value = self.tail
        curr_head = self.head
        while curr_head.next != self.tail:
            curr_head = curr_head.next
        self.tail = curr_head
        return ret_value



    def get_size(self):
        pass


    def __str__(self):
        curr_head = self.head
        ret_str = ""
        while curr_head != self.tail:
            ret_str += f"{curr_head} "
            curr_head = curr_head.next
        ret_str += f"{curr_head}"
        return ret_str


my_list = LinkedList()
my_list.push_front(1)
my_list.push_front(12)
my_list.push_front(2)
my_list.push_front(13)
print(my_list)
# my_list.push_back(12)
x = my_list.pop_back()
print(x)
print(my_list)



