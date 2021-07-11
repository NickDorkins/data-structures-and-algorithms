# from queue import Queue

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left =  left
        self.right = right
        # print('NODE TEST VALUE:', self.value)
        # print('NODE TEST LEFT:', self.left)
        # print('NODE TEST RIGHT:', self.right)

class BinaryTree:
    
    def __init__(self, root = None):
        self.root = root
        # print('BinTree TEST ROOT VALUE:', self.root)

#  Write custom ERROR's for any that are raised
    
    
    
    def preOrder(self):
        if self.root is None:
            return "Your Root is empty, please preLoad a root value."
        # print('SELF ROOT TEST', self.root)
        list_of_nodes_preorder = []
        def traverse(root):
            list_of_nodes_preorder.append(root.value)
        #     # if not root:
        #     #     return 
            # print('ROOT VALUE INSIDE PREORDER:', root.value)
            if root.left:
                traverse(root.left)
                # print('ROOT LEFT VALUE INSIDE PREORDER:', root.left.value)
            if root.right:
                traverse(root.right)
                # print('ROOT RIGHT VALUE INSIDE PREORDER:', root.right.value)
            # print('RETURNED LIST:' ,list_of_nodes_preorder)
        # print('ROOT VALUE INSIDE PREORDER END:', self.root)
        traverse(self.root)
        return list_of_nodes_preorder
    
    
    # NOTE TO SLLEPY NICK: DON'T TRY TO PASS A LIST IN AS A TREE!!! 

    # LOOK AT THE NODE VALUE BEING PASSED IN AND ASSIGN IT TO ROOT, LEFT, OR RIGHT

    # DON'T FORGET TO PASS THE VALUES INTO NODE()


# def FizzBuzzTree(tree):
#     bin_tree = BinaryTree()
#     root = bin_tree.root
#     # This statement should change a value to "FIZZBUZZ" if it is a Modulo of both 3 and 5
#     if root.value %15 == 0:

#        pass
    
#     # This statement should change a value to "BUZZ" if it is a Modulo of 5
#     if root.value %5 == 0:
#         pass

#     # This statement should change a value to "FIZZ" if it is a Modulo of 3
#     if root.value %3 == 0:
#         pass
    
#     pass


def fizzBuzzTree(tree):
    newTree = BinaryTree()
    newTree.root = fizz_buzz_helper(tree.root)
    return newTree

def fizz_buzz_helper(root):
    newNode = None
    if root is None: 
        return "Root is empty"    
    if root.nodeVal % 15 == 0:
        newNode = Node('FizzBuzz')
    elif root.nodeVal % 3 == 0:
        newNode = Node('Fizz')            
    elif root.nodeVal % 5 == 0:
        newNode = Node('Buzz')   
    else: 
        newNode = Node(root.nodeVal)
    if root.left is not None:
        newNode.left = fizz_buzz_helper(root.left)
    if root.right is not None:
        newNode.right = fizz_buzz_helper(root.right)
    return newNode

# def FizzBuzzTree(tree):
#     bin_tree = BinaryTree()
#     # bin_tree.root = tree_translator()
#     return bin_tree

#     def tree_translator(root):
#         fizz_buzz_node = None

#         if root is None:
#             return "Your Root is empty, please add a root value. (FizzBuzz)" 

#         if root != None:
#             if root.value %15 == 0:
#                 fizz_buzz_node = Node('FIZZBUZZ')
#             elif root.value %5 == 0:
#                 fizz_buzz_node = Node('BUZZ')
#             elif root.value %3 == 0:
#                 fizz_buzz_node = Node('FIZZ')
#             else:
#                 fizz_buzz_node = Node(root.value)
#             if root.left is not None:
#                 fizz_buzz_node.left =  root.left
#             if root.right is not None:
#                 fizz_buzz_node.right = root.right
#         return fizz_buzz_node
#         print('FIZZ_BUZZ_NODE', fizz_buzz_node)

        # if right != None:
        #     if right %15 == 0:
        #         fizz_buzz_list.append('FIZZBUZZ')
        #     elif right %5 == 0:
        #         fizz_buzz_list.append('BUZZ')
        #     elif right %3 == 0:
        #         fizz_buzz_list.append('FIZZ')
        #     else:
        #         fizz_buzz_list.append(right.value)
    


if __name__ == "__main__":
    
    one = Node(1)
    three = Node(3)
    five = Node(5)
    eight = Node(8)
    ten = Node(10)
    fifteen = Node(15)
    sixty = Node(60)


    tree = BinaryTree(one)
    tree.root.left = three
    tree.root.right = five
    tree.root.left.left = eight
    tree.root.left.right = ten
    tree.root.right.left = fifteen
    tree.root.right.right = sixty

    tree = fizzBuzzTree(one)
    tree.root.left = three
    tree.root.right = five
    tree.root.left.left = eight
    tree.root.left.right = ten
    tree.root.right.left = fifteen
    tree.root.right.right = sixty

    # tree = tree_translator(one)
    # tree.root.left = three
    # tree.root.right = five
    # tree.root.left.left = eight
    # tree.root.left.right = ten
    # tree.root.right.left = fifteen
    # tree.root.right.right = sixty

    tree.preOrder()
    print('PRINT PREORDER TEST', tree.preOrder())

    fizzBuzzTree()
    print('FIZZ.BUZZ.TREE TEST', fizzBuzzTree(tree.preOrder))

    # tree_translator()
    # print('FIZZ.BUZZ.TREE.TRANSLATOR TEST', tree_translator())