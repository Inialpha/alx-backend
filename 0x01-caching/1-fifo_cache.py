#!/usr/bin/env python3
""" module for the FIFOCache class """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ cacheing using the FIFO algorithm """
    def __init__(self):
        """ initialize the class instance """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                pop_key, value = self.cache_data.popitem(last=False)
                print(f"DISCARD {pop_key}")

        def get(self, key):
            """ return the value in self.cache_data linked to key """
            return self.cache_data.get(key)
