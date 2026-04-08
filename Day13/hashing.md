# Hash Tables and Hashing in Python

This note explains hashing, hash tables, Python `dict`, and Python `set` in a structured way with examples, steps, and common use cases.

## Contents

1. What Is Hashing?
2. What Is a Hash Table?
3. Python Hash-Based Structures
4. Hash Function in Python
5. Dictionary Internal Working
6. Collision Handling
7. Dictionary Example
8. Set Explanation
9. Why Hashing Is Fast
10. Time Complexity
11. Practical Programs
12. Important Rules
13. Memory and Resizing
14. `dict` vs `set`
15. Interview Focus
16. Final Summary
17. Additional Programs

## 1. What Is Hashing?

Hashing is a technique that maps a key to an array position using a hash function.

### Core Idea

`Key -> Hash Function -> Index -> Store or Retrieve Value`

### Example

`"apple" -> hash("apple") -> 102 -> store at index 102`

Hashing avoids scanning the entire data structure, which makes lookup very fast in average cases.

## 2. What Is a Hash Table?

A hash table is a data structure that:

- Stores data internally using array-like slots
- Uses a hash function to decide where data should go
- Supports fast insert, search, update, and delete operations

### Conceptual Structure

| Index | Key     | Value |
|-------|---------|-------|
| 0     | None    | None  |
| 1     | `cat`   | 5     |
| 2     | None    | None  |
| 3     | `apple` | 10    |
| 4     | None    | None  |

## 3. Python Hash-Based Structures

Python provides two main built-in hash-based structures:

| Structure | Purpose |
|-----------|---------|
| `dict`    | Stores key-value pairs |
| `set`     | Stores unique keys only |

## 4. Hash Function in Python

Python uses the built-in `hash()` function.

```python
print(hash("apple"))
print(hash(10))
```

### Notes

- `hash()` returns an integer
- Python uses that integer internally to compute a storage location
- The actual index depends on the current table size

## 5. Dictionary Internal Working

### Example Dictionary

```python
data = {
    "apple": 10,
    "banana": 20,
}
```

### Insertion Steps

For this statement:

```python
data["apple"] = 10
```

Python conceptually performs these steps:

1. Compute the hash value of the key.
2. Convert that hash into an index using the current table size.
3. Store the key and value in that slot.

### Conceptual Example

```python
hash("apple") -> 23456789
index = hash("apple") % table_size
table[index] = ("apple", 10)
```

### Access Steps

For this lookup:

```python
data["apple"]
```

Python conceptually:

1. Computes the hash of `"apple"`
2. Finds the related index
3. Returns the stored value

This is why lookup is usually $O(1)$.

### Update

```python
data["apple"] = 50
```

If the key already exists, Python updates the value.

### Delete

```python
del data["apple"]
```

This removes the key-value pair from the dictionary.

## 6. Collision Handling

### What Is a Collision?

A collision happens when two different keys map to the same index.

### Example

```python
hash("cat") % size == 3
hash("bat") % size == 3
```

Both keys want the same position.

### How Python Handles It

Python dictionaries use open addressing with probing.

If one position is occupied, Python checks other positions until it finds a valid slot.

### Conceptual Example

1. Index `3` is occupied
2. Check the next possible position
3. Store the item in an available slot

### Important Point

Too many collisions reduce performance, which is why resizing matters.

## 7. Dictionary Example

```python
data = {}

# Insert
data["a"] = 1
data["b"] = 2

# Access
print(data["a"])

# Update
data["a"] = 10

# Delete
del data["b"]

print(data)
```

### Output

```python
1
{'a': 10}
```

## 8. Set Explanation

A set stores only unique values.

You can think of it conceptually as a dictionary with keys only.

### Example

```python
s = {1, 2, 3}
```

Conceptually:

```python
{1: None, 2: None, 3: None}
```

### Common Operations

```python
s.add(4)
s.remove(2)
print(3 in s)
```

### Duplicate Handling

```python
s = {1, 2, 2, 3}
print(s)
```

Output:

```python
{1, 2, 3}
```

Sets automatically remove duplicates.

## 9. Why Hashing Is Fast

Without hashing, search often takes $O(n)$ because each element may need to be checked.

With hashing, search is usually $O(1)$ because Python can go directly to the expected storage location.

## 10. Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert    | $O(1)$       | $O(n)$     |
| Search    | $O(1)$       | $O(n)$     |
| Delete    | $O(1)$       | $O(n)$     |

Worst-case performance appears when there are many collisions.

## 11. Practical Programs

### 1. Frequency Count

```python
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for value in arr:
    freq[value] = freq.get(value, 0) + 1

print(freq)
```

### 2. Two Sum Problem

```python
def two_sum(arr, target):
    seen = {}

    for index, num in enumerate(arr):
        diff = target - num

        if diff in seen:
            return [seen[diff], index]

        seen[num] = index


print(two_sum([2, 7, 11, 15], 9))
```

### 3. Remove Duplicates

```python
arr = [1, 1, 2, 3, 3]
unique = list(set(arr))
print(unique)
```

## 12. Important Rules

### Keys Must Be Immutable

Allowed key types:

- `int`
- `str`
- `tuple`

Not allowed as dictionary keys:

- `list`
- `dict`

### Invalid Example

```python
data = {[1, 2]: "value"}  # Error
```

Lists are mutable, so they cannot be hashed safely for dictionary keys.

## 13. Memory and Resizing

When a dictionary becomes crowded, Python increases its internal table size and rehashes existing elements.

This helps keep average-case operations fast.

## 14. `dict` vs `set`

| Feature | `dict` | `set` |
|---------|--------|-------|
| Stores  | Key and value | Only keys |
| Duplicate keys | Not allowed | Not allowed |
| Lookup | $O(1)$ average | $O(1)$ average |
| Main use | Mapping data | Keeping unique items |

## 15. Interview Focus

### Why Use Hashing?

- Fast lookup
- Efficient updates
- Useful for large inputs

### Common Interview Problems

- Two Sum
- Frequency counting
- Duplicate detection
- Anagram checking

## 16. Final Summary

- Hashing maps a key to an index
- A hash table stores data using that mapping
- Python `dict` and `set` are hash-based data structures
- Average insert, search, and delete are usually $O(1)$
- Collisions are handled internally

## 17. Additional Programs

### Program 1: First Repeated Element

```python
def first_repeated(arr):
    seen = set()

    for value in arr:
        if value in seen:
            return value
        seen.add(value)

    return None


print(first_repeated([4, 6, 1, 6, 9]))
```

### Program 2: Check if Two Strings Are Anagrams

```python
def are_anagrams(first, second):
    if len(first) != len(second):
        return False

    count = {}

    for ch in first:
        count[ch] = count.get(ch, 0) + 1

    for ch in second:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return not count


print(are_anagrams("listen", "silent"))
```

### Program 3: Find Common Elements in Two Lists

```python
def common_elements(list1, list2):
    return list(set(list1) & set(list2))


print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
```

## Hashing Flow Diagram

```mermaid
flowchart LR
    A[Key] --> B[hash(key)]
    B --> C[Compute Index]
    C --> D[Store or Retrieve Value]
```
