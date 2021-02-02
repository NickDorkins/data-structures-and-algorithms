class Node:
    def __inti__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    
    def __init__(self, root = None):
        self.root = root

#  Write custom ERROR's for any that are raised

    def preOrder(self):
        if self.root is None:
            return "Your Root is empty, please preLoad a root value."
        def traverse(root):
            if not root:
                return
            print(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)

    def inOrder(self):
        if self.root is None:
            return "Your Root is empty,inOrder to proceed, please add a root value."
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            print(root.value)
            traverse(root.right)

    def postOrder(self):
        if self.root is None:
            return "Your Root is empty, please add a root value."
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            traverse(root.right)
            print(root.value)


    #  Can assume all values are numeric
    def find_maximum_value(self):
        if self.root is None:
            return "Your Root is empty, to find the max value, please add a root value."
        def traverse(root):
            if not root:
                return
            max_value = 0
            if max_value == 0:
                max_value = root.value
            if max_value != 0:
                if root.left < max_value:
                    traverse(root.left)
                if root.left > max_value:
                    max_value = root.left
                    traverse(root.left)
                if root.right < max_value:
                    traverse(root.right)
                if root.right > max_value:
                    max_value = root.right
                    traverse(root.right)
        traverse(self.root)
       