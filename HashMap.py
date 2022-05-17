
class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [ [] for i in range(array_size)]


    def hash(self, key):
        my_hash = key.encode()
        return sum(my_hash)

    def compress(self, my_hash):
        return my_hash % self.array_size

# Assigns by appending the key value pair to the end of the list, unless it has the same key, in which case overwrites the value..
    def assign(self, key, value):
#if_all is a variable that returns True only if the value does not overwrite something else in the list, or if the keyval pair wasnt placed in an empty slot. this allows us to know when to append to the end of the list.
        if_all = True
        array_index = self.compress(self.hash(key))

        if self.array[array_index] == []:
            self.array[array_index].append([key, value])
            if_all = False
        for tuples in self.array[array_index]:
            if tuples[0] == key:
                tuples[1] = value
                if_all = False
        if if_all:
            self.array[array_index].append([key, value])

# Retrieves values by looping through the list at index self.array[array_index]
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))

# TESTING PURPOSES ONLY
        for i in self.array:
            print(i)
# </TESTING PURPOSES ONLY>
        if len(self.array[array_index]) >= 1:
            for keyval in self.array[array_index]:
                if keyval[0] == key:
                    return keyval[1]
#TESTS
new_hash = HashMap(7)

new_hash.assign('test', 'case')
new_hash.assign('testing', 'casing')
new_hash.assign('testing', 'purple')
new_hash.assign('pink', 'tester')
new_hash.assign('butts', 'random')
print(new_hash.retrieve('testing'))
#print(new_hash.retrieve('test'))
