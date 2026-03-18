def merge_sort(arr):
    # Base case: a list with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Divide: find the middle point and split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer: recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combine: merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged_list = []
    i = 0 # pointer for the left list
    j = 0 # pointer for the right list

    # Compare elements from both lists and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # If one list is exhausted, add the remaining elements from the other list
    while i < len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list

# Driver program to test the code
if __name__ == '__main__':
    my_list = [12, 11, 13, 5, 6, 7]
    print(f"Given list is: {my_list}")
    sorted_list = merge_sort(my_list)
    print(f"Sorted list is: {sorted_list}")
