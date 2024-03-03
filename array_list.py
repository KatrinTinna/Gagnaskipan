class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
    pass


class NotOrdered(Exception):
    pass


class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.ordered = True

    # Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for i in range(self.size):
            if i == self.size - 1:
                return_string += f"{self.arr[i]}"
            else:
                return_string += f"{self.arr[i]}, "
        return return_string

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.resize()
        self.size += 1
        self.ordered = False
        for i in range(self.size - 2, -1, -1):
            self.arr[i + 1] = self.arr[i]
        self.arr[0] = value

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        self.resize()
        self.size += 1
        self.ordered = False
        for i in range(self.size - 2, index - 1, -1):
            self.arr[i + 1] = self.arr[i]
        self.arr[index] = value

    # Time complexity: O(1) - constant time
    def append(self, value):
        self.ordered = False
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()
        else:
            self.ordered = False
            self.arr[index] = value

    # Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.arr[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()
        else:
            return self.arr[index]

    # Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.arr[self.size - 1]

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp_arr = [None] * self.capacity
            for i in range(self.size):
                temp_arr[i] = self.arr[i]
            self.arr = temp_arr

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        self.ordered = False
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()
        else:
            for i in range(index, self.size-1):
                self.arr[i] = self.arr[i + 1]
        self.size -= 1

    # Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.ordered = True

    # Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        self.resize()
        if self.ordered != True:
            raise NotOrdered()
        elif self.size == 0:
            self.prepend(value)
        else:
            for num in range(self.size):
                if num == 0:
                    if value < self.arr[num]:
                        self.prepend(value)
                        break
                if num == self.size - 1:
                    if value > self.arr[num]:
                        self.append(value)
                        break
                else:
                    if self.arr[num] <= value <= self.arr[num + 1]:
                        self.insert(value, num + 1)
                        break
        self.ordered = True

 
        
    def _ordered_find(self, value, my_list, low , high):
        
            middle = (high+low) // 2
            if high == low and my_list[middle] != value:
                raise NotFound()
            if my_list[middle] == value:
                return middle
            elif value > my_list[middle]:
                return self._ordered_find(value, my_list, middle+1, high)
            else:
                return self._ordered_find(value, my_list, low, middle-1)
        
    def _unordered_find(self, value, my_list, index):
            if index >= self.size:
                raise NotFound()
            elif my_list[index] == value:
                return index
            else:
                return self._unordered_find(value, my_list, index +1)


    def find(self, value):
            if self.size == 0:
                raise NotFound()
            if self.ordered:
                index = self._ordered_find(value, self.arr, 0, self.size-1)
            else:
                index = self._unordered_find(value, self.arr,0)
            return index
    
    # Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        index_value = self.find(value)
        self.remove_at(index_value)

if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
    x = ArrayList()
    x.append(1)
    x.append(2)
    x.append(3)
    x.prepend(100)
    print(x)
    x.remove_largest()
    print(x)

   

 