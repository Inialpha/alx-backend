#!/usr/bin/env python3
""" module for the LIFOCache class """
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ cacheing using the LIFO algorithm """
    def __init__(self):
        """ initialize the class instance """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    pop_key, value = self.cache_data.popitem()
                    print(f"DISCARD: {pop_key}")
                else:
                    self.cache_data.pop(key)
            self.cache_data[key] = item
            self.cache_data.move_to_end

        def get(self, key):
            """ return the value in self.cache_data linked to key """
            return self.cache_data.get(key)
