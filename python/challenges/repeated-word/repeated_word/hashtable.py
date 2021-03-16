from repeated_word.linkedlist import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self. _buckets = size * [None]
        
    def _hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        primed = sum * 19
        index = primed % self.size
        return index

    def add (self, key, value):
        hashed_key_index = self._hash(key)

        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].add((key, value))

    def get(self, requested_key):
        index_of_key = self._hash(requested_key)
        if self._buckets[index_of_key]:
            bucket_linked_list = self._buckets[index_of_key]
            current = bucket_linked_list.head

        while current:
            if current.value.key == requested_key:
                return current.value.value
            current = current.next 
        return False



    def contains(self, key):
        if self.get(key) is None:
            return False
        else:
            return True
      




#  ------------------ Class HashTable Notes --------------

# How many buckets do you want?
# You have to create a new hashtable and rerun KVP if you want to increase/decrease table size

    # takes in an arbitrary key and returns an index in the collection.

    # Factor in hashtable length

    # Max index = HT len -1

    # Use prime number to mutiply

    # Must be 0 or greater >=0


# --------------------- add() method Notes-------------------

    # takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
    # Hash the Key
    # Check the Index(bucket) for existing value

        # Check bucket to see if it's empty

        # if empty create linkedlist, otherwise ADD to linkedlist

        # when you add to the LL you must pass in the Key and Value to the add() method


# ---------------------- get() method Notes -----------------

    # takes in the key and returns the value from the table.

        # Dictionary Get Method

        # Run requested_key through the _hash() method

        # Assign bucket to a temp variable with the hashed index

        # Check if the index is empty 

        # assign something to the head of the LinkedList 'Current'       

        # (key, value) this is going to be the value of each LL

        # current.data[0] = key

        # current.data[1] = value

        # Does the key in the LinkedList = requested_key

        # return value

        # current = current.next

        # Once you find the matching key return the requested_key and exit - no longer need to keep checking

# ------------------- get() method Notes --------------------

    # takes in the key and returns a boolean, indicating if the key exists in the table already.

        #  Similar to get

        # Don't return value 

        # Return a boolean (True or False)
