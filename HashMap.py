
class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [ [] for i in range(array_size)]

    def hash(self, key):
        my_hash = key.encode()
        return sum(my_hash)

    def compress(self, my_hash):
        return my_hash % self.array_size

# Assigns by appending the key value pair to the end of the list, be it empty or not.
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))

        if self.array[array_index] == []:
            self.array[array_index].append([key, value])
            print(self.array[array_index])
            return
        for tuplepair in self.array[array_index]:
            if tuplepair[0] == key:
                tuplepair[1] = value
                return

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))

        if len(self.array[array_index]) >= 1:
            for keyval in self.array[array_index]:
                if keyval[0] == key:
                    return keyval[1]


new_hash = HashMap(10)

new_hash.assign('penis', 'balls')

print(new_hash.retrieve('penis'))
