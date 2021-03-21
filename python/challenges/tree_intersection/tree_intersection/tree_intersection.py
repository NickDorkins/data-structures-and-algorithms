class Node:
    def __inti__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    
    def __init__(self, root = None):
        self.root = root

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

def tree_intersection(tree1, tree2):
    match = []
    t1v = tree1.preOrder()
    t2v = tree2.preOrder()
    current1 = tree1.root
    current2 = tree2.root

    if current1 is None or current2 is None:
        return "Cannot compare an empty tree."
    for value in t1v:
        if value in t2v:
            if value in match:
                continue
            else:
                match.append(value)
        else:
            continue
    if len(match) == 0:
        return "No matches found between the input values."
    else:
        return match
