class Stack:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity


    def push(self,value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

 


    def pop(self):
        # temp_arr = [None]*self.capacity
        # start = 0
        # end = self.size
        # for i in range(self.size-1):
        #     temp_arr[i] = self.arr[i]
        value_to_return = self.arr[self.size-1]
        # self.arr = temp_arr
        
        self.size -= 1
        return value_to_return
            
    

    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp_arr = [None] * self.capacity
            for i in range(self.size):
                temp_arr[i] = self.arr[i]
            self.arr = temp_arr
    
    def __str__(self):
        str_to_return = ""
        for i in range(self.size):
            if i != None:
                str_to_return += f"{self.arr[i]} "
        return str_to_return


   

stack =Stack()
print(stack)
stack.push(3)
print(stack)
stack.push(5)
print(stack)
stack.push(11)
print(stack)
x = stack.pop()
print(stack)

# stack.push(11)
# print(stack)
# stack.push(12)
# print(stack)
# # stack.push(11)
# print(stack)
