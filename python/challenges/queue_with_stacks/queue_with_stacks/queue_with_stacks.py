


class InvalidOperationError(BaseException):
    pass

class PseudoQueue:

    def __init__(self, node = None):
        self.front = node
        self.rear = node

    def enqueue(self, front):
        node = Node(front)
        if self.is_empty() is True:
            self.front = node
            return node
        self.front.next = node
        return node

    def dequeue(self):
        remove = self.rear
        if self.is_empty() is True:
            raise InvalidOperationError("Method not allowed on empty collection")
        self.rear = self.rear.next
        remove.next = None
        self.rear = None
        return remove.value