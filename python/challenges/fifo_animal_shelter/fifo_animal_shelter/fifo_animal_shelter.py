class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class AnimalShelter():

    def __init__(self, node = None):
        self.front = node
        self.rear = node

    def enqueue(self, animal):
        new_node = Node(animal)
        if animal == "":
            raise InvalidOperationError("Please input a valid animal.")
        elif animal != "cat" and animal != "dog":
            raise InvalidOperationError("Please input a valid animal.")

        if self.is_empty() is True:
            self.rear = new_node
            self.front = new_node
            return new_node
        elif self.is_empty() is False:
            self.rear.next = new_node
            self.rear = new_node
            return new_node





    def is_empty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False