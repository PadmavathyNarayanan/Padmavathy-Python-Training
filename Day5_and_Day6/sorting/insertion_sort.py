def insertionSort(arr):
    n = len(arr)
    
    if n <= 1:
        return
    
    # Traverse from second element
    for i in range(1, n):
        
        # Store current element to be inserted
        key = arr[i] 
        
        # Compare with previous elements        
        j = i - 1
        
        # Shift elements greater than key
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
            
        # insert key at correct position
        arr[j + 1] = key      


arr = [12, 11, 13, 5, -1]
insertionSort(arr)
print(arr)