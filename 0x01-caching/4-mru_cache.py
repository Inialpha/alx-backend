#!/usr/bin/env python3
""" module for the MRUCache class """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ cacheing using the MRU algorithm """

    def __init__(self):
        """ initialize the class instance """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key """
        if key and item:
            if len(
                    self.cache_data) >= BaseCaching.MAX_ITEMS \
                            and key not in self.cache_data:
                pop_key, value = self.cache_data.popitem(False)
                print(f"DISCARD: {pop_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, False)

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
