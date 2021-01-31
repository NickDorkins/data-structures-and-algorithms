class Node:
    def __inti__(self, values = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    
    def __init__(self, root = None):
        self.root = root

    def preOrder(self):
        def traverse(root):
            if not root:
                return
            print(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)

    def inOrder(self):
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            print(root.value)
            traverse(root.right)

    def postOrder(self):
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            traverse(root.right)
            print(root.value)

#  Write custom ERROR's for any that are raised

class BinarySearch:

    def add(self):
        pass

    def contains(self):
        pass

