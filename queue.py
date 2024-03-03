class Queue:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.head = 0
        self.tail = 0



    def add(self,value):
        #udated tail
        self.resize()
        
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        # self.tail += 1


    def remove(self):
        value = self.arr[self.head]
        self.head += (self.head + 1) % self.capacity     
        # if self.size != 0:
        #     for i in range(start, end):
        #         self.arr[i-1] = self.arr[i]
        self.size -= 1
        return value
            


    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp_arr = [None] * self.capacity
            counter = 0
            for i in range(self.head, self.size):
                temp_arr[counter] = self.arr[i]
                counter += 1
            
            self.arr = temp_arr
            self.tail = self.size
            self.head = 0


    def __str__(self):
        
        str_to_return = ""
        if self.head >= self.tail:
            for i in range(self.head, self.capacity):
                str_to_return += f"{self.arr[i]} "
                for i in range(self.tail):
                    str_to_return += f"{self.arr[i]} "
        else:
            for i in range(self.head, self.tail):
                str_to_return += f"{self.arr[i]} "
        return str_to_return
    

queue = Queue()
queue.add(5)
queue.add(7)
queue.add(2)
queue.add(1)
