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




    
            
              
      

n = Node(4)
# print(type(n))
# print_all(n)
n= push_front(n, 11)
n= push_front(n, 70)
n = push_front(n,3)
print_all(n)
print()
print()

# print_all(n)
# print()
n = push_back(n,111)
print_all(n)
n = remove_last(n)
print()
print_all(n)
n = push_front(n,4)
print()
print_all(n)
# n = remove(n)
# print_all(n)
# print()
# n = remove(n)
# print_all(n)
# print()
# n = remove(n)
# print_all(n)
# print()
# n = remove(n)
# print_all(n)
# print_recursive(n)



