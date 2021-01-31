from tree import __version__
from tree.tree import Node, BinarySearch, BinaryTree

def test_version():
    assert __version__ == '0.1.0'


# Can successfully instantiate an empty tree
def successfully_instantiate_an_empty_tree():
    tree = BinaryTree()
    expected = None
    actual = tree.root.value
    assert actual == expected


# # Can successfully instantiate a tree with a single root node
# def instantiate_a_tree_with_a_single_root_node():
#     a = Node("A")
#     pass

# # Can successfully add a left child and right child to a single root node
# def successfully_instantiate_an_empty_tree():
#     a = Node("A")
#     b = Node("B")
#     c = Node("C")
#     d = Node("D")
#     e = Node("E")
#     f = Node("F")

# # Can successfully return a collection from a preorder traversal
# def successfully_instantiate_an_empty_tree():
#     a = Node("A")
#     b = Node("B")
#     c = Node("C")
#     d = Node("D")
#     e = Node("E")
#     f = Node("F")

# # Can successfully return a collection from an inorder traversal
# def successfully_instantiate_an_empty_tree():
#     a = Node("A")
#     b = Node("B")
#     c = Node("C")
#     d = Node("D")
#     e = Node("E")
#     f = Node("F")

# # Can successfully return a collection from a postorder traversal
# def successfully_instantiate_an_empty_tree():
#     a = Node("A")
#     b = Node("B")
#     c = Node("C")
#     d = Node("D")
#     e = Node("E")
#     f = Node("F")