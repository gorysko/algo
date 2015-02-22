"""Quick sort algo"""

__author__ = "gorysko@gmail.com"
__description__ = "Quck sort algo for stanford course on coursera"

counter = 0

def _partition(array, first, second):
	"""Partition part of algorithm."""
	item = array[second]
	index = first - 1
	global counter
	counter += second - first

	for num in range(first, second):
		if array[num] <= item:
			index += 1
			array[index], array[num] = array[num], array[index]
	array[index + 1], array[second] = array[second], array[index + 1]

	return index + 1

def quicksort(array, first, second):
	"""quicksort algo."""
	if first < second:
		index = _partition(array, first, second)
		quicksort(array, first, index - 1)
		quicksort(array, index + 1, second)
	return array

if __name__ == '__main__':
	raw = open('../input__10.txt')
	data = [int(i.strip()) for i in raw.readlines()]
	raw.close()
	print data
	print quicksort(data, 0, len(data) - 1)
	print counter
