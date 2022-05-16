
class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [ None for i in range(array_size)

    def hash(self, key):
        my_hash = key.encode()
        return sum(my_hash)

    def compress(self, my_hash):
        return my_hash % self.array_size

    def assign(self, key, value):
        
