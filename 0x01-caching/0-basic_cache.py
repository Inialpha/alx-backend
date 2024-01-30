#!/usr/bin/env python3
""" module for the BasicCache class """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ define BasicCache """

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key.
        """

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        return self.cache_data.get(key)
