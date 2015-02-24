"""Counting sort algo implementation"""

__author__ = "gorysko@gmail.com"
__description__ = "Counting sort implementation for pronetheus"

def counting_sort(array):
    """in-place counting sort"""
    length = max(array) + 1
    temp = [0] * length
    for index in array:
        temp[index] += 1
    index = 0
    for item in range(length):
        for _ in range(temp[item]):
            array[index] = item
            index += 1
    return array


if __name__ == '__main__':
    print counting_sort([2, 5, 3, 0, 2, 3, 0, 3])
