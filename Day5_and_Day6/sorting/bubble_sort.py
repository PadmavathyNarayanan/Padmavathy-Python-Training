def bubbleSort(arr):
    print(f'Input array {arr}')
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        print(f'\t Current i-th iteration at {i} is {arr[i]}')
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            print(f'\t Current j-th iteration {j} is {arr[j]}, {arr[j+1]}')
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            print(f'Modified array {arr}') 
        if not swapped:
            break 

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)