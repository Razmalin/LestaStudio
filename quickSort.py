import random


def findPivot(begin, end):
    return random.randint(begin, end)
    # return begin


def partition(array, begin, end, *, reverse=False):
    pivotIdx = findPivot(begin, end)
    pivot = array[pivotIdx]

    array[end], array[pivotIdx] = array[pivotIdx], array[end]
    firstLarger = begin
    for idx in range(begin, end):
        if reverse ^ (array[idx] <= pivot):
            array[idx], array[firstLarger] = array[firstLarger], array[idx]
            firstLarger += 1

    array[end], array[firstLarger] = array[firstLarger], array[end]
    return firstLarger


def quickSort(array, begin=0, end=None, *, reverse=False):
    if end is None:
        end = len(array) - 1

    if begin < end:
        mid = partition(array, begin, end, reverse=reverse)
        quickSort(array, begin, mid - 1, reverse=reverse)
        quickSort(array, mid + 1, end, reverse=reverse)


if __name__ == '__main__':
    a = [3, 4, 6, 3, 1, 2, 5, 9]
    quickSort(a, reverse=True)
    print(a)