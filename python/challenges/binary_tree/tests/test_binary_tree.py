from binary_tree import __version__
from binary_tree.binary_tree import Node, BinaryTree

def test_version():
    assert __version__ == '0.1.0'


def test_return_max_value_of_a_tree():
    tree = BinaryTree(1)
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    expected = 3
    actual = tree.max_value
    assert actual == expected