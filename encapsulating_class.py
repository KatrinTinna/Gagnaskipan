import typing
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    
def push_front(head, data):
        n = Node(data, head)
        return n
    
def print_all(head : Node):
        while head != None:
              print(head.data)
              head = head.next

def print_recursive(head : Node):
      if head != None:
            print(head.data)
            print_recursive(head.next)




def remove(head : Node):
      head = head.next
      return head

def push_back(head : Node, value):
      if head == None:
            return Node(value, None)
      head.next = push_back(head.next, value)
      return head

def remove_last(head : Node):
      if head.next == None:
            return None
      head.next = remove_last(head.next)
      return head



class Stack:
    def __init__(self, head = None):
        self.head = head

    def push(self, data):
        if self.head == None:
            n = Node(data)
            self.head = n
        else:
            n = Node(data)
            n.next = self.head
            self.head = n 
    
    
    # def print_recursivex(self, head):
    #   if self.head != None:
    #         print(head.data)
    #         self.print_recursivex(head.next)
    


    def pop(self):
        return_val = self.head
        self.head = self.head.next
        return return_val

    def get_size(self):
        counter = 0
        head = self.head
        while self.head != None:
             counter += 1
             self.head = self.head.next
        self.head = head
        return counter
            
    
    def __str__(self) -> str:
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str



stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(5)
x = stack.pop()
x = stack.get_size()
print("hallo",x)
x = stack.pop()
print(x.data)
print(stack)


# def push_front(self, data):
#         # if self.head == None:
#         n = Node(data)
#         n.next = self.head
#         self.head = n
#         return n


class Queue:
    def __init__(self, tail = None, head = None):
        self.tail = tail
        self.head = head



    def push_back(self, data):
        if self.head == None:
            n = Node(data)
            self.head = n
        else:
            if self.head.next == None:
                
                n = Node(data)
                self.head.next = n
                self.tail = n
            else:
                self.head.next = self.push_back(data)
            


    def pop(self):
        pass


    def get_size(self):
        pass


    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
             


queue = Queue()
queue.push_back(69)
print(queue)
queue.push_back(3)
print(queue)
queue.push_back(40)

print(queue)