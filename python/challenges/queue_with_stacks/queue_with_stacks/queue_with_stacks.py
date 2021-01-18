class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class PseudoQueue():
    
    def __init__(self, node = None):
        self.front = node
        self.rear = node

    def enqueue(self, rear):
        node = Node(rear)
        if self.is_empty() is True:
            self.rear = node
            self.front = node
            return node
        self.front.next = node
        return node

    def dequeue(self):
        remove = self.front
        if self.is_empty() is True:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            self.front = self.front.next
            remove.next = None
            self.front = None
            return remove.value

    def is_empty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False

class Stack():

    def __init__(self, node = None):
        self.top = node

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.top
        self.top = self.top.next 
        return node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False