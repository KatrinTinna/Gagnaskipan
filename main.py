class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class Empty(Exception):
    pass


class NotOrdered(Exception):
    pass

class BSTMap_Node:
    def __init__(self,key = None, data = None, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    
    def insert(self, key, data):
        self.root = self._insert(key, data, self.root)

    def _insert(self, key, data, node):
        if node == None:
            self.size += 1
            return BSTMap_Node(key,data)
        elif key < node.key:
            node.left = self._insert(key,data, node.left)
        elif key > node.key:
            node.right = self._insert(key,data, node.right)
        else:
            raise ItemExistsException()
        return node
    

    def update(self, key, data):
        self.root = self._update(key, data, self.root)
    

    def _update(self, key, data, node):
        if node.key == key:
            node.data = data
        elif key < node.key:
            node.left = self._update(key, data, node.left)
        elif key > node.key:
            node.right = self._insert(key, data, node.right)
        else:
            raise NotFoundException()
        return node


    # def print_inorder(self):
    #     ret_str = ""
    #     self.inorder(self.root, ret_str)


    def _inorder(self,node):
        if node == None:
            return ""
        left = self._inorder(node.left)
        right = self._inorder(node.right)
        return f" {left}{{{node.key} : {node.data}}}{right} "

    def find(self, key):
        self.root = self._find(key, self.root) 

    def _find(self, key, node):
        if node.key == key:
            return node.value
        elif key < node.key:
            node.left = self._find(key, node.left)
        elif key > node.key:
            node.right = self._find(key, node.right)
        else:
            raise NotFoundException()
        
    def contains(self, key):
        return self._contains(key, self.root)
       
    
        

    def _contains(self, key, node):
        if node == None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._contains(key, node.left)
        else:
            return self._contains(key, node.right)
     
        
    
    def remove(self,key):
        pass

    def __setitem__(self,key, data):
        my_node = self.root
        while my_node != None:
            if my_node.key == key:
                my_node.data = data
                return
            elif key < my_node.key:
                my_node = my_node.left
            else:
                my_node = my_node.right
        self.insert(key,data)
        

    def __getitem__(self,key):
        my_node = self.root
        while my_node != None:
            if my_node.key == key:
                return my_node.data
            elif key < my_node.key:
                my_node = my_node.left
            else:
                my_node = my_node.right
        raise NotFoundException()

    def __len__(self):
        return self.size
    








    def __str__(self):
        return self._inorder(self.root)


x = BSTMap()
x.insert(1, "A")
x.insert(5, "B")
x.insert(3, "C")
x.insert(11, "D")
x.insert(12, "D")
x.update(1,"DD")
print(x)
x[15] = "Katrín"

print(x)
print(len(x))
print(x)


    


