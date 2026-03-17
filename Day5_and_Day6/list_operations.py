li = [1,2,3,4,5,5,5]

# add elements to a list
li.append(6)
li.append('hello')
li.extend([7,8,9,11])

print('After adding elements:', li)

# remove elements from the list
li.remove('hello')

print('After removing the element from list:', li)

# using pop
rmv_idx = 3
li.pop(rmv_idx)

print('After removing/pop the element from list:', li)

# using slice operator `::`
rev_li = li[::-1]
print(f'Reversing the list: {rev_li}')

# accessing the list elements
len_li = len(rev_li)
print(f'Length of the list {len_li}')

search_idx = 6
if search_idx < len_li-1:
    print(f'Accessing element at idx {search_idx} is {rev_li[search_idx]}')
else:
    print('Index not found')

# update the list elements using index
rev_li[search_idx] = 13
print(f'After modifying the list element at pos {search_idx} is {rev_li}')
rev_li[search_idx] = 'world'
print(f'After modifying the list element at pos {search_idx} is {rev_li}')

# Find the index of the list
idx = rev_li.index('world')
print(f'World is found at idx {idx}')

# count of elements in the list
cnt_ele_five = rev_li.count(5)
print(f'Counf of element 5 is {cnt_ele_five}')

for i in rev_li[5:]:
    print(f'Count of ele {i} is {rev_li.count(i)}')

out_li = [i if i != 'world' else -1 for i in rev_li ]
print(out_li)