"""Merge and sort algo"""

__author__ = "gorysko@gmail.com"
__description__ = "Merge and sort algo for stanford course on coursera"

counter = 0

def merge_sort(array):
    """Meerge and sort algo."""
    
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = array[middle:]
    right = array[:middle]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(right, left)

def merge(left, right):
    """merges arrays"""
    global counter
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        elif left[0] > right[0]:            
            result.append(right[0])
            right = right[1:]
            counter += len(left)
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    return result

