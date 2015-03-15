"""Counting sort algo implementation"""

__author__ = "gorysko@gmail.com"
__description__ = "Counting sort implementation for pronetheus"

def counting_sort(array):
    """counting sort"""
    indexes = {}
    result = [0] * len(array)
    dif = max(array) - min(array) + 1
    count = [0] * dif

    for j in range(len(array)):
        count[array[j]] += 1

    for item in range(1, dif):
        count[item] += count[item - 1]
    for k in range(len(array))[::-1]:
        indexes[k] = count[array[k]] - 1
        result[count[array[k]] - 1] = array[k]
        count[array[k]] -= 1
    return result, indexes


def radix_sort(array):
    """radix sort implementation."""
    length = len(array[0])
    first = ord('a')
    last = ord('z')
    num = last - first + 1
    buckets = [[]] * num
    counter = 0
    for position in range(length)[::-1]:
        counter += 1
        for string in array:
            buckets[ord(string[position]) - first].append(string)
            print buckets
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
        if counter == 1:
            return array
    return array

if __name__ == "__main__":
    f = open('../anagrams.txt')
    data = [i.strip() for i in f.readlines()]
    f.close()
    L = ['joe',
    'bob',
    'rot',
    'roc',
    'mar', 'suz', 'sue']
    L = radix_sort(L)
    print L
