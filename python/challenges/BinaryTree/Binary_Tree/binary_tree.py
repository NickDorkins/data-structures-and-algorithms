from queue import Queue

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

    def breadth_first_traversal(self):
        if self.root is None:
            return "Your Root is empty, please add a root value. (Breadth First Traversal)" 
        
        q = Queue()
        q.enqueue(self.root)
        traversal_order = []

        while len(q) > 0:
            current = q.dequeue()
            if current is None:
                return traversal_order
            traversal_order.append(current.value)

            if current.left != None:
                q.enqueue(current.left.value)

            if current.right != None:
                q.enqueue(current.right.value)
        
        return traversal_order


       



# test_tree = BinaryTree()
# test_tree.root = Node(1)
# test_tree.root.left = Node(2)
# test_tree.root.right = Node(3)
# test_tree.root.left.left = Node(4)
# test_tree.root.left.right = Node(5)
# test_tree.root.right.left = Node(6)
# test_tree.root.right.right = Node(7)

# print(test_tree.breadth_first_traversal)

