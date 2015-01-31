INVERSIONS = 0

def merge_sort(array):
    """Meerge and sort algo."""
    if len(array) <= 1:
        return array
    middle = len(array) / 2
    left = array[middle:]
    right = array[:middle]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    """merges arrays"""
    global INVERSIONS
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            INVERSIONS += 1
            result.append(right[0])
            right = right[1:]
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    return result

if __name__ == '__main__':
    raw = open("ints.txt")
    data = [int(x) for x in raw]
    raw.close()
    finished = merge_sort(data)
    print finished == data.sort()
    print INVERSIONS

