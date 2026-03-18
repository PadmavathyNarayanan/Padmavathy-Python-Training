def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # choose last element as pivot

    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [8, 3, 1, 7, 0, 10, 2]

sorted_arr = quick_sort(arr)

print("Sorted Array:", sorted_arr)