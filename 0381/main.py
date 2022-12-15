# 381. Insert Delete GetRandom O(1) - Duplicates allowed
import random

class RandomizedCollection:
    def __init__(self):
        self.hashmap = {} # <key integer value> = set (integer indices)
        self.array = []
                
    def insert(self, val: int) -> bool:
        is_not_present = False

        if val not in self.hashmap:
            self.hashmap[val] = set()
            is_not_present = True

        self.hashmap[val].add(len(self.array)) # next index is added to hashmap
        self.array.append(val)

        return is_not_present

    def remove(self, val: int) -> bool:
        is_removed = False  

        if val in self.hashmap:
            remove_index = next(iter(self.hashmap[val]))
            last_index = len(self.array)-1
            last_val = self.array[last_index]

            self.hashmap[val].remove(remove_index)
            self.hashmap[last_val].add(remove_index)
            self.hashmap[last_val].remove(last_index)
            if len(self.hashmap[val]) == 0:
                del self.hashmap[val] # remove key,value pair from dict

            # swap and remove from the array
            self.array[remove_index], self.array[last_index] = self.array[last_index], self.array[remove_index]
            self.array = self.array[:len(self.array)-1]  # remove the value at the end

            is_removed = True
        
        return is_removed

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.array)-1)
        return self.array[random_index]