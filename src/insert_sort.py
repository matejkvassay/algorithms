def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j>=0 and array[j]>key:
            array[j+1] = array[j]
            j -= 1
        array[j+1]=key

if __name__ == "__main__":
    array = [7,2,5,14,3,8,1,4]
    print(f"Input array: {array}")
    insert_sort(array)
    print(f"Sorted array: {array}")