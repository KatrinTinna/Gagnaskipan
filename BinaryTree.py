class BT_Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    

class BinaryTree:
    def __init__(self):
        self.root = None

    

    

    def popluate_tree_recur(self):
        value = input("Enter node value ")
        if value == "":
            return None
        left = self.popluate_tree_recur()
        right = self.popluate_tree_recur()
        return BT_Node(value, left,right)
    
    def populate_tree(self):
        self.root = self.popluate_tree_recur()

    

    def preorder(self, node):
        if node == None:
            return
        print(str(node.data), end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def print_preorder(self):
        self.preorder(self.root)

    def print_inorder(self):
        self.inorder(self.root)

    def print_postorder(self):
        self.postorder(self.root)

    
    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data, end = " ")
        self.inorder(node.right)

    def postorder(self,node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(f"{node.data} ", end = " ")

    def call_count_instances(self, value):
        x = self.count_instances(value, self.root)
        return x

    def count_instances(self, value, node):
        if node == None:
            return
        self.count_instances(value, node.left)
        self.count_instances(value, node.right)
        if node.data == value:
            return 1
                   

        
        

tree = BinaryTree()
tree.populate_tree()
tree.print_preorder()
x = tree.call_count_instances(1)
print()
print(x)


class G_T_Node():
    def __init__(self,data = None):
        self.data = data
        self.arr = []


class GeneralTree:
    def __init__(self):
        self.root = None


    def populate_tree(self):
        level = 0
        self.root = self.populate_tree_recur(level)
        


    
    def populate_tree_recur(self, level = 0):
        value = input("Enter node value: ")
        level += 1
        if value == "":
            return None
        new_node = G_T_Node(value)
        while True:
            child_note = self.populate_tree_recur(level)
            if child_note == None:
                break
            new_node.arr.append(child_note)
        return new_node
            
        

                
            # if value == None:
            #     return
            # new_node = G_T_Node(value)
            # while True:
            #     if 
            #     self.populate_tree_recur(new_node)


    def print_preorder(self):
        self.preorder(self.root)


    def preorder(self, node):
        print(str(node.data), end=" ")
        for i in node.arr:
            self.preorder(i)

    #Inorder á ekki við í general tree

    def print_postorder(self):
        self.postorder(self.root)

    def postorder(self, node):
        for i in node.arr:
            self.postorder(i)
        print(node.data, end = " ")


# general = GeneralTree()
# general.populate_tree()
# general.print_preorder()