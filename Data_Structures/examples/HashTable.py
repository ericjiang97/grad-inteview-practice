# Not guaranteed to work as this is a blind solution

class HashTable:
    def __init__(self, size, b):
        '''
        Initalising Function
        :param size: The size of the list
        '''
        self.size = size
        self.b = b
        self.data = [None] * self.size
        self.collision = 0
    
    def hashfunction(self,word):
        '''
        Calculates the hash value for the given word.
        :param key: the key 
        :return: the hashed value
        :comp: Average: O(n), Best: O(1), Worst: O(n)
        '''
        a = 16259208967579 # a is a very large prime
        value = 0
        for i in range(len(word)):
            value = (a * value + ord(word[i])) % self. size
            a = a * self.b % (self.size - 1)
        return value
    