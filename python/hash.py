"""Counting sort algo implementation"""

__author__ = "gorysko@gmail.com"
__description__ = "Simple hash table implementation for prometheus"


def hash_insert(lst, item, size):
    """Hash insert function.
    Args:
        lst: array to set element
        item: value to set into array
        size: size of the array
    """
    index = 0
    while index != size:
        hashed = hashing(item, size)
        if lst[hashed] == None:
            lst[hashed] = item
        else:
            index += 1


def hash_search(lst, item, size):
    """Hash search function.
    Args:
        lst: array to set element
        item: value to set into array
        size: size of the array
    Returns:
        Value if it was found or None
    """
    index = 0
    while index != size:
        hashed = hashing(item, size)
        if lst[hashed] == item or lst[hashed] == None:
            return hashed
        index += 1
    return None


def hashing(item, size):
    """Divide model of hashing."""
    return item % size

if __name__ == '__main__':
    f = open('../test_06.txt')
    data = [int(i.strip()) for i in f.readlines()]
    f.close()

    size_test = len(data)
    test = [None] * size_test

    print 'working...'
    for value in data:
        hash_insert(test, value, size_test)
    print 'finished!'
    print test[-1]
