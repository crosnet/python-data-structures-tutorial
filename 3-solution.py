"""
CSE 212
BYU-Idaho
Author: Emmanuel Odonkor
queue-tutorial  Problem - solution
"""

class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        #before we insert a value, we compare it to the parent node
        # which in this case is the root node.
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else: 
                    self.right.insert(data)
        else:
            self.data = data
    #we need to create a function to print the nodes
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
    #traversing forward the the BST
    def TraverseForward(self, root):
        #create an empty array to hold the values
        result = []
        if root:
            result.append(root.data)
            result = result + self.TraverseForward(root.left)
            result = result + self.TraverseForward(root.right)
        return result
#now let's add some numbers and display them
BST = BinarySearchTree(18)
BST.insert(6)
BST.insert(15)
BST.insert(11)
BST.insert(3)
BST.PrintTree()
print("Traverse Forward")
print(BST.TraverseForward(BST))
