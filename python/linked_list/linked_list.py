
class Node:
    
    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.nextNodeValue = None




class LinkedList:
    
    def __init__(self):
        self.head = None

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


# assign variable to current node value
# create empty list
# while loop through values and append to empty list
# reassign the created variable to next value
# if next value is None append "none" to the end of the string
# return stringified list

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


      
