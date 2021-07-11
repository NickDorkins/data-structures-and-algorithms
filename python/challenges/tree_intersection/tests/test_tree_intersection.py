from tree_intersection.tree_intersection import tree_intersection, BinaryTree, Node



def test_regular_trees():
    treeOne = BinaryTree()
    treeOne.root = Node(1)
    treeOne.root.left = Node(2)
    treeOne.root.right = Node(3)

    treeTwo = BinaryTree()
    treeTwo.root = Node(2)
    treeTwo.root.left = Node(3)
    treeTwo.root.right = Node(5)

    expected = [2, 3]
    actual = tree_intersection(treeOne, treeTwo)
    assert actual == expected