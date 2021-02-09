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

    

def FizzBuzzTree(tree):
    bin_tree = BinaryTree()
    bin_tree.root = tree_translator(tree.root)
    return bin_tree

def tree_translator(root):
    fizz_buzz_node = None

    if root is None:
        return "Your Root is empty, please add a root value. (FizzBuzz)" 

    if root != None:
        if root.value %15 == 0:
            fizz_buzz_node = Node('FIZZBUZZ')
        elif root.value %5 == 0:
            fizz_buzz_node = Node('BUZZ')
        elif root.value %3 == 0:
            rfizz_buzz_node = Node('FIZZ')
        else:
            fizz_buzz_node = Node(root.value)
    return fizz_buzz_node
    print('FIZZ_BUZZ_NODE', fizz_buzz_node)

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

    tree = FizzBuzzTree(one)
    tree.root.left = three
    tree.root.right = five
    tree.root.left.left = eight
    tree.root.left.right = ten
    tree.root.right.left = fifteen
    tree.root.right.right = sixty

    tree = tree_translator(one)
    tree.root.left = three
    tree.root.right = five
    tree.root.left.left = eight
    tree.root.left.right = ten
    tree.root.right.left = fifteen
    tree.root.right.right = sixty

    tree.preOrder()
    print('PRINT PREORDER TEST', tree.preOrder())

    FizzBuzzTree()
    print('FIZZ.BUZZ.TREE TEST', FizzBuzzTree())

    tree_translator()
    print('FIZZ.BUZZ.TREE TEST', tree_translator())