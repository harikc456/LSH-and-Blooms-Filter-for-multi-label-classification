import mmh3
import numpy as np

class BloomsFilter():
    
    def __init__(self, false_positive ,n_items):
        self.false_positive = false_positive
        self.n_items = n_items
        self.bit_array_size = int(self.calculate_bit_array_size())
        self.bit_array = np.zeros(self.bit_array_size)
        self.n_hash = int(self.find_optimum_hash_functions())
        self.primes = self.generate_primes_for_hashes()
    
    def calculate_bit_array_size(self):
        m = -1 * self.n_items * np.log(self.false_positive) / (np.log(2) * np.log(2))
        return m
    
    def find_optimum_hash_functions(self):
        k = np.log(2) * (self.bit_array_size/self.n_items)
        return k
    
    def generate_primes(self, start ,end):
        primes = []
        for val in range(start, end + 1): 
            if val > 1: 
                for n in range(2, val//2 + 2): 
                    if (val % n) == 0: 
                        break
                    else: 
                        if n == val//2 + 1: 
                            primes.append(val) 
        return primes
    
    def generate_primes_for_hashes(self):
        primes = self.generate_primes(self.bit_array_size - 1000,self.bit_array_size)
        return primes[-self.n_hash:]
    
    def hash_functions(self,word):
        for prime in self.primes:
            index = mmh3.hash(word, signed=False) % prime
            self.bit_array[index] = 1
    
    def predict(self,word):
        for prime in self.primes:
            index = mmh3.hash(word, signed=False) % prime
            if self.bit_array[index] == 0:
                return 0
        return 1
