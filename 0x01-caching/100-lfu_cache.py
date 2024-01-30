#!/usr/bin/env python3
""" module for the LFUCache class """
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ cacheing using the LRU algorithm """

    def __init__(self):
        """ initialize the class instance """
        self._frequency = OrderedDict()
        super().__init__()
        self.cache_data = OrderedDict()

    def min_keys(self):
        """ return minimum keys """
        min_value = min(self._frequency.values())
        return [key for key, value in self._frequency.items() if value ==
                min_value]

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key """
        if key and item:

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_keys = self.min_keys()
                pop_key = min_keys[-1]
                self.cache_data.pop(pop_key)
                self._frequency.pop(pop_key)
                print(f"DISCARD: {pop_key}")
            if key in self._frequency:
                self._frequency[key] += 1
                self._frequency.move_to_end(key, last=False)
            else:
                self._frequency[key] = 1
                self._frequency.move_to_end(key, last=False)

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            if key in self._frequency:
                self._frequency[key] += 1
                self._frequency.move_to_end(key, last=False)
            else:
                self._frequency[key] = 1
                self._frequency.move_to_end(key, last=False)
        return self.cache_data.get(key)
