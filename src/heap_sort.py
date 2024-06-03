def parent(i):
    if i == 0:
        return -1
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, heap_size, i):
    """
    O(log(N))
    """
    l = left(i)
    r = right(i)
    largest = i
    # find largest element out of parent/left/right
    if l < heap_size and A[l] > A[i]:
        largest = l

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, heap_size, largest)


def build_max_heap(A):
    """
    O(N*log(N))
    """
    for i in range((len(A) // 2) + 1, -1, -1):
        max_heapify(A, len(A), i)


def heap_sort(A):
    """
    O(N*log(N))
    """
    heap_size = len(A)
    build_max_heap(A)  # O(N*log(N))
    for i in range(heap_size - 1, 0, -1):  # O(N*log(N))
        A[heap_size - 1], A[0] = A[0], A[heap_size - 1]
        heap_size -= 1
        max_heapify(A, heap_size, 0)
    return A


heap = [1, 4, 2, 8, 3, 6, 5]
print(f'original elements: {heap}')
heap_sort(heap)
print(f'sorted elements: {heap}')
