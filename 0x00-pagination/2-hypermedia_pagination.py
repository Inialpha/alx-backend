#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple of size two containing a
    start index and an end index """
    return ((page - 1) * page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page """
        assert type(page) is int and \
            page > 0 and type(page_size) is int and page_size > 0
        res = index_range(page, page_size)
        data = self.dataset()

        return data[res[0]: res[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Hypermedia pagination """

        next_page = page + 1
        prev_page = page - 1

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page > len(data):
            next_page = None
        if page < 2:
            prev_page = None
        res = {'page_size': len(data), 'page': page,
               'data': data, 'next_page': next_page,
               'prev_page': prev_page, 'total_pages': total_pages}

        return res
