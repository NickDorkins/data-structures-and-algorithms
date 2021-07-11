from Breadth_First.breadth_first import BinaryTree, Node


def test_breadth_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    expected = [1, 2, 3, 4, 5, 6, 7]
    actual = tree.breadth_first_traversal()
    assert actual == expected 
