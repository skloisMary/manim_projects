# bubbleSort
def bubbleSort():
    # unsorted array
    arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
    length = len(arr)
    # External circulation for length-1 times
    for i in range(length - 1):
        # Internal circulation
        for j in range(length - 1 - i):
            if arr[j] > arr[j+1]:
                # swap
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j+1] = tmp
    return arr # sorted array in ascending order
