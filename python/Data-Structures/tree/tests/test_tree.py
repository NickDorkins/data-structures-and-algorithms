
# import pytest
from tree import __version__
from tree.tree import Node, BinaryTree, BinarySearch

def test_version():
    assert __version__ == '0.1.0'


# Can successfully instantiate an empty tree
def successfully_instantiate_an_empty_tree():
    tree = BinaryTree()
    expected = None
    actual = tree.root.value
    assert actual == expected


# Can successfully instantiate a tree with a single root node
def instantiate_a_tree_with_a_single_root_node():
    tree = BinaryTree("A")
    tree.root = Node("A")
    expected = "A"
    actual = tree.root.value
    assert actual == expected

# # Can successfully add a left child and right child to a single root node
def add_a_left_child_and_right_child_to_a_single_root_node():
    tree = BinaryTree("A")
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    expected = "B" and "C"
    actual = tree.root.left.value and tree.root.right.value
    assert actual == expected

# # Can successfully return a collection from a preorder traversal
# def return_a_collection_from_a_preorder_traversal():
#     

# # Can successfully return a collection from an inorder traversal
# def return_a_collection_from_an_inorder_traversal():
#    

# # Can successfully return a collection from a postorder traversal
# def return_a_collection_from_a_postorder_traversal():
#     