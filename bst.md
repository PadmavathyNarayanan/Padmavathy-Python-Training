# Binary Search Tree (BST) operations

1. Concept
2. Example input & working
3. Python code
4. Explanation


---

### What is a Binary Search Tree (BST)?

A BST is a binary tree where:
- Left child < Parent
- Right child > Parent

**Example:**

        10
       /  \
      5    15
     / \    \
    2   7    20


---

### **1. INSERT Operation**

**Input Example:**

Insert values: 10, 5, 15, 2, 7, 20

**Working:**

- Insert 10 → becomes root
- Insert 5 → less than 10 → goes left
- Insert 15 → greater than 10 → goes right
- Insert 2 → left of 5
- Insert 7 → right of 5
- Insert 20 → right of 15


```python
def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root
```

---

### **2. SEARCH Operation**

**Example:**

- Search for 7

**Working:**

- Start at root (10)
    - 7 < 10 → go left
    - 7 > 5 → go right
- Found at node 7

```python
def search(self, root, key):
        if root is None or root.value == key:
            return root

        if key < root.value:
            return self.search(root.left, key)

        return self.search(root.right, key)
```

---

### **3. DELETE Operation**

**Cases:**
1. Node is leaf → remove directly
2. Node has one child → replace with child
3. Node has two children → replace with inorder successor (smallest in right subtree)

**Example:**
- Delete 5
- Node 5 has two children (2 and 7)
- Replace with inorder successor → 7
- Remove original 7

```python
    # FIND MIN (successor - for delete)
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # FIND MAX (predecessor - for delete)
    def find_max(self, root):
        while root.right:
            root = root.right
        return root

    # DELETE
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)

        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: Node with one child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Case 3: Node with two children (inorder-successor)
            successor = self.find_min(root.right)
            root.value = successor.value
            root.right = self.delete(root.right, successor.value)

            # Case 4: Node with two children (inorder-predecessor)
            predecessor = self.find_max(root.left)
            root.value = predecessor.value
            root.left = self.delete(root.left, predecessor.value)

        return root
```

---

### **4. FIND HEIGHT**

`Height = number of levels (or max depth)`

**In Example tree:**
    `Height = 3`

```python
def height(self, root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
```

---

### **5. CHECK BALANCED**

A tree is balanced if:

`|height(left) - height(right)| ≤ 1 for every node`

```python
def is_balanced(self, root):
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)
```
---

### **PYTHON PROGRAM**

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    # SEARCH
    def search(self, root, key):
        if root is None or root.value == key:
            return root

        if key < root.value:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # FIND MIN (for delete)
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # DELETE
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)

        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Case 2: Two children
            successor = self.find_min(root.right)
            root.value = successor.value
            root.right = self.delete(root.right, successor.value)

        return root

    # HEIGHT
    def height(self, root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    # CHECK BALANCED
    def is_balanced(self, root):
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)


# ---------------- MAIN ----------------

bst = BST()

values = [10, 5, 15, 2, 7, 20]

for v in values:
    bst.root = bst.insert(bst.root, v)

# SEARCH
result = bst.search(bst.root, 7)
print("Found" if result else "Not Found")

# DELETE
bst.root = bst.delete(bst.root, 5)

# HEIGHT
print("Height:", bst.height(bst.root))

# BALANCED CHECK
print("Balanced:", bst.is_balanced(bst.root))
```

---

### **STEP-BY-STEP EXPLANATION**

#### **Insert Function**

```python
if root is None:
    return Node(value)
```

- If tree is empty → create node

```python
if value < root.value:
    go left
else:
    go right
```

---

#### **Search Function**

- Compare value
- Move left or right
- Stop when found or None

---

#### **Delete Function**


**Case 1: Leaf node**
-    `return None`

**Case 2: One child**
-   `return child`

**Case 3: Two children**
- `replace with smallest in right subtree`


---

#### **Height Function**

`height = 1 + max(left, right)`


---

#### **Balanced Check**

```python
if abs(left_height - right_height) > 1:
    return False
```

---

#### **Sample Output**

```
Found
Height: 3
Balanced: True
```

---

### **Real-Time Use Cases**

- Database indexing
- File systems
- Search engines
- Auto-suggestions
