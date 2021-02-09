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
        return list_of_nodes_preorder
        traverse(self.root)
    

def FizzBuzzTree(self):
    
    if self.root is None:
        return "Your Root is empty, please add a root value. (FizzBuzz)" 

        fizz_buzz_list = []

        if left != None:
            if left %15 == 0:
                q.enqueue('FIZZBUZZ')
            elif left %5 == 0:
                q.enqueue('BUZZ')
            elif left %3 == 0:
                q.enqueue('FIZZ')
            else:
                q.enqueue(current.left.value)

        if current.right != None:
            if right %15 == 0:
                q.enqueue('FIZZBUZZ')
            elif right %5 == 0:
                q.enqueue('BUZZ')
            elif right %3 == 0:
                q.enqueue('FIZZ')
            else:
                q.enqueue(current.right.value)
    
    return fizz_buzz_list



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

    tree.preOrder()
