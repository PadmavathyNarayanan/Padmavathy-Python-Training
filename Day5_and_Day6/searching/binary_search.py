li = [2, 12, 15, 17, 27]
target = 17



def binary_search(li, target):
    low = 0
    high = len(li) - 1
    for i,j in enumerate(li):
        mid = (low + high) // 2
        print(f'At idx {i}, low {low}, mid {mid}, high {high} ')
        if li[mid] == target:
            return i
        elif li[mid] < target:
            print(f'\t{li[mid]} < {target} in {li}')
            low = mid + 1
            print(f'\tlow {low} mid {mid} high {high}')
        elif li[mid] > target:
            print(f'\t{li[mid]} > {target} in {li}')
            high = mid - 1
            print(f'\tlow {low} mid {mid} high {high}')
    return -1



result = binary_search(li, target)
print(50*'-')
print(f'Result: {result}')
print(50*'-')