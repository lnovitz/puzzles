from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # capacity initialize
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache or len(self.cache.keys()) < self.capacity:
            self.cache[key] = value
        else:
            # get rid of least recently used key
            self.cache.popitem(last=False) # index        
            self.cache[key] = value
        self.cache.move_to_end(key)