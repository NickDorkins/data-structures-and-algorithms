
class Node:
    
    def __init__(self, nodeValue=None, nextNodeValue=None):
        self.nodeValue = nodeValue
        self.nextNodeValue = nextNodeValue




class LinkedList:
    
    def __init__(self):
        self.head = None


    def __str__():
        compareValue = self.head.nodeValue
        appendedValue = "{" + self.head.nodeValue + "} ->"
        stringifiedList = []
        while compareValue is not None:
            stringifiedList.append(appendedValue)
            compareValue = self.head.nextNodeValue
        if compareValue is None:
            stringifiedList.append("none")
        return(strinigifiedList)


    def insert(self, value):
        stringifiedValue = str(value)
        node = Node(stringifiedValue)

        if self.head is not None:
            node.nextNodeValue = self.head
        self.head = node


    def includes(self, value):
        headVal = self.head
        if headVal == None:
            return False
        while headVal != None:
            if headVal.nodeValue != value and headVal.nextNodeValue == None:
                return False
            elif value == headVal.nodeValue:
                return True
            elif value != headVal.nodeValue:
                headVal = headVal.nextNodeValue


    def append(self, value):
        current = self.head
        if current == None:
            self.head = Node(value)
        while current:
            if current.nextNodeValue == None:
                node = Node(value)
                current.nextNodeValue = node
                return
            else:
                current = current.nextNodeValue


    def insertBefore(self, value, newVal):
            current = self.head
            if current == None:
                self.head = Node(value)
            elif current.nodeValue == value:
                self.insert(newVal)
                return
            while current:
                if current.nextNodeValue.nodeValue == value:
                    beforeVal = current.nextNodeValue
                    current.nextNodeValue = Node(newVal, beforeVal)
                    return
                elif current.nextNodeValue.nodeValue != value:
                    current = current.nextNodeValue
                else:
                    return "EXCEPTION"
            

    def insertAfter(self, value, newVal):
        current = self.head
        if current == None:
            self.head = Node(value)
        while current:
            if current.nodeValue == value:
                afterVal = current.nextNodeValue
                current.nextNodeValue = Node(newVal, afterVal)
                return
            elif current.nodeValue != value:
                current = current.nextNodeValue
            else:
                return "EXCEPTION"


# Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

# Create a separate list
# Iterate throught the current list and append current to new list 
# Find the negative kth index
# Return the value of the index

    def kthHelper(self):
        emptyList = []
        current = self.head
        while current:
            emptyList.append(current.nodeValue)
            current = current.nextNodeValue
        return emptyList

    def kthFromEnd(self, k):
        helper = self.kthHelper()
        length = (len(helper)-1)-k
        if k < len(helper) and k >= 0:
            return helper[length]
        else:
            return "EXCEPTION"    
