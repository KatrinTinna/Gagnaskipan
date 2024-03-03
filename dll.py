
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self, data = None, next = None, prev = None):
        self.tail = Node()
        self.head = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current_node = self.tail

    def insert(self, data):
        prev = self.current_node.prev
        next = self.current_node
        new_node = Node(data)
        new_node.next = next
        new_node.prev = prev
        prev.next = new_node
        next.prev = new_node
        self.current_node = new_node

    def remove(self):
        if self.current_node != self.tail:
            prev = self.current_node.prev
            next = self.current_node.next
            prev.next = next
            next.prev = prev
            self.current_node = next
          

    def get_value(self):
        if self.current_node == self.tail:
            return None
        else:
            return self.current_node.data

    def move_to_next(self):
        if self.current_node != self.tail:
            self.current_node = self.current_node.next

    def move_to_prev(self):
        if self.current_node.prev != self.head:
            self.current_node = self.current_node.prev

    def move_to_pos(self, pos):
        counter = 0
        if (pos >= 0) and  pos <= len(self):
            curr_head = self.head.next
            while counter < pos:
                curr_head = curr_head.next
                counter += 1
            self.current_node = curr_head

    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current_node = self.tail

    def get_first_node(self):
        if self.head.next == self.tail:
            return None
        else:
            return self.head.next


    def get_last_node(self):
        if self.tail.prev == self.head:
            return None
        else:
            return self.tail.prev

    def partition(self, low, high):
        self.current_node = low.next
        curr_head = low.next
        while curr_head != high.next:
            if curr_head.data < low.data:
                temp = curr_head.next
                data = curr_head.data
                self.current_node = curr_head
                self.remove()

                self.current_node = low
                self.insert(data)
                curr_head = curr_head.next
                self.current_node = temp
            else:
                curr_head = curr_head.next
        self.current_node = low
        return low


    def quicksort(self, low, high):
        
        almost_low = low.prev
        almost_high = high.next
        pivot = self.partition(low, high)
        if almost_low.next != pivot:
            self.quicksort(almost_low.next,pivot.prev)
        if pivot.next != almost_high: 
            self.quicksort(pivot.next, almost_high.prev)
        



    def sort(self):
        if len(self) > 0:
            self.quicksort(self.get_first_node(), self.get_last_node())
        self.current_node = self.head.next


    def __len__(self):
        size = 0
        curr_head = self.head.next
        while curr_head != self.tail:
            size += 1
            curr_head = curr_head.next
        return size

    def __str__(self):
        ret_str = ""
        curr_head = self.head.next
        while curr_head != self.tail:
            ret_str += f"{curr_head.data} "
            curr_head = curr_head.next
        return ret_str

if __name__ == "__main__":
    #create tests here if you want
    pass
    x = DLL()
  

   
   

    
    

    
