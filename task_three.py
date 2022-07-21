# Само условие задания говорит о том, что стандартный quicksort не подойдет.
# Introsort использует быструю сортировку (quicksort) и переключается на пирамидальную
# сортировку, когда глубина рекурсии превысит некоторый заранее
# установленный уровень (например, логарифм от числа сортируемых элементов).
# Этот подход сочетает в себе достоинства обоих методов с худшим случаем O(n log n)
# и быстродействием, сравнимым с быстрой сортировкой.


from heapSort import heapSort
from quickSort import partition
from math import log2


def introSort(array, begin=0, end=None, depth=0, *, reverse=False):
    if end is None:
        end = len(array) - 1

    if depth < log2(len(array)):
        if begin < end:
            mid = partition(array, begin, end)
            introSort(array, begin, mid - 1, depth + 1)
            introSort(array, mid + 1, end, depth + 1)
    else:
        array[begin:end + 1] = heapSort(array[begin:end + 1])


if __name__ == '__main__':
    a = [3, 1, 9, 4, 7, 2, 8, 6, 5]
    introSort(a)
    print(a)
