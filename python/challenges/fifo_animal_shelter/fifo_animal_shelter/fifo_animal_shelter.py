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
            raise InvalidOperationError("User input cannot be empty.")
        elif animal != "cat" and animal != "dog":
            raise InvalidOperationError("Valid input is either 'cat' or 'dog'.")

        if self.is_empty() is True:
            self.rear = new_node
            self.front = new_node
            return new_node
        elif self.is_empty() is False:
            self.rear.next = new_node
            self.rear = new_node
            return new_node

    def dequeue(self, pref):
        current = self.front
        if pref == "":
            raise InvalidOperationError("Please enter your prefernce of 'cat' or 'dog'.")
        elif self.is_empty() is True:
            raise InvalidOperationError("All of our furry friends have found homes, please try agin later.")
        elif pref != "cat" and pref != "dog":
            raise InvalidOperationError("We only have 'cats' and 'dogs' at our shelter, please choose one.")
        else:
            while current:
                if current == pref:
                    return pref
                elif current != pref:
                    current = current.next
                else:
                    raise InvalidOperationError(f"We do not currently have any {pref}'s available for adoption today.")



            # Loop through queue until preference value is found
            # while pref == "cat":
            #     if current == "cat":
            #         current.next = self.front
            #         return current





    def is_empty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False