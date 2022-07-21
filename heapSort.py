def percolateDown(heap, idx, maxIdx=None, *, reverse=False):
    if maxIdx is None:
        maxIdx = len(heap) - 1
    while idx < maxIdx:
        largestIdx = idx
        if 2 * idx + 1 <= maxIdx and (reverse ^ (heap[2 * idx + 1] > heap[largestIdx])):
            largestIdx = 2 * idx + 1
        if 2 * idx + 2 <= maxIdx and (reverse ^ (heap[2 * idx + 2] > heap[largestIdx])):
            largestIdx = 2 * idx + 2

        if largestIdx != idx:
            heap[idx], heap[largestIdx] = heap[largestIdx], heap[idx]
            idx = largestIdx
        else:
            break


def heapify(heap, maxIdx=None, *, reverse=False):
    if maxIdx is None:
        maxIdx = len(heap) - 1
    for idx in range(maxIdx // 2, -1, -1):
        percolateDown(heap, idx, reverse=reverse)


def heapSort(heap, reverse=False):
    heapify(heap, reverse=reverse)
    for idx in range(len(heap) - 1, 0, -1):
        heap[0], heap[idx] = heap[idx], heap[0]
        percolateDown(heap, 0, idx - 1, reverse=reverse)
    return heap


if __name__ == '__main__':
    a = [3, 4, 6, 3, 1, 2, 5, 9]
    heapSort(a, reverse=True)
    print(a)