def insert_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


if __name__ == "__main__":
    array = [7, 2, 5, 14, 3, 8, 1, 4]
    print(f"Input array: {array}")
    insert_sort(array)
    print(f"Sorted array: {array}")
