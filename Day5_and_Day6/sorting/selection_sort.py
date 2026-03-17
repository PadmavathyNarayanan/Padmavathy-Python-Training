def selectionSort(array, size):
    for ind in range(size):
        # Assume current index has the minimum value
        min_index = ind

        # Find the minimum element in remaining unsorted array
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        array[ind], array[min_index] = array[min_index], array[ind]

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)

print(arr)