# AVL Tree operations


---

### **What is an AVL Tree?**

- An AVL Tree is a self-balancing Binary Search Tree (BST).

**For every node:**

`Height difference (Balance Factor) = height(left) - height(right)`

- Must be in {-1, 0, +1}
- If it goes beyond → we rebalance using rotations


---

### **AVL Tree Operations**

1. Insert
2. Delete
3. Search
4. Get Height
5. Check Balance
6. Rotations (LL, RR, LR, RL)

---

### **Working Methodology (INSERT)**

**Example Input:**

**Insert:** 10, 20, 30

---

**Step 1: Insert 10**

**Tree:**
10

`Balanced: YES`


---

**Step 2: Insert 20**

10
  \
   20

`Balance factor of 10 = -1 → YES`


---

**Step 3: Insert 30**

10
  \
   20
     \
      30

`Balance factor of 10 = -2 -> NO (Unbalanced)`

**Case:** Right-Right (RR)
**Solution:** Left Rotation

**After rotation:**

```
      20
    /   \
   10     30
```

`Balanced again -> YES`


---

### **Rotations Explained**
1. Left Rotation (RR Case)
2. Right Rotation (LL Case)
3. Left-Right Rotation (LR Case)
    - Left rotate child
    - Then right rotate parent
4. Right-Left Rotation (RL Case)
    - Right rotate child
    - Then left rotate parent

---

### **Python Implementation**

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
```

---

#### **Helper Functions**

```python
def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)
```

---

#### **Rotations**

- **Right Rotation**

```python
def right_rotate(y):
    x = y.left
    T2 = x.right

    # Rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x
```

---

#### **Left Rotation**

```python
def left_rotate(x):
    y = x.right
    T2 = y.left

    # Rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y
```

---

### **Insert Operation**

```python
def insert(root, key):
    # Step 1: Normal BST insert
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Step 2: Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Step 3: Get balance
    balance = get_balance(root)

    # Step 4: Balance cases

    # LL Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # RR Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # LR Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
```

---

### **Search Operation**

```python
def search(root, key):
    if not root or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)
```

---

### **Inorder Traversal (to verify BST)**

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
```

---

**Example Execution**

```python
root = None
values = [10, 20, 30]

for v in values:
    root = insert(root, v)

print("Inorder Traversal:")
inorder(root)
```

**Output:**

`10 20 30`

- Tree is balanced automatically


---

### **Summary**

Operation Time Complexity
- Insert O(log n)
- Delete O(log n)
- Search O(log n)

---

**Key Understanding**

- `AVL tree = BST + self balancing`
- After every insert/delete:
    - Check balance factor
    - Apply rotation if needed

Rotations keep tree height small → faster operations


#### Full AVL Tree Python Code with

- Insert
- Delete
- Search
- Height & Balance
- Traversals
- Example usage

---


```python

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    #  Get height
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    #  Get balance factor
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    #  Right rotation (LL case)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    #  Left rotation (RR case)
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    #  Insert
    def insert(self, root, key):

        # Step 1: BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get balance
        balance = self.get_balance(root)

        # Step 4: Balance cases

        # LL
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    #  Get minimum node
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    #  Delete
    def delete(self, root, key):

        # Step 1: BST delete
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # Node with 1 or 0 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with 2 children
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Step 2: Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get balance
        balance = self.get_balance(root)

        # Step 4: Balance cases

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    #  Search
    def search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    #  Traversals
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# =========================
#  Example Usage
# =========================

if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Insert values
    values = [10, 20, 30, 40, 50, 25]
    for v in values:
        root = avl.insert(root, v)

    print("Inorder Traversal:")
    avl.inorder(root)

    print("\nPreorder Traversal:")
    avl.preorder(root)

    # Search
    key = 25
    result = avl.search(root, key)
    print("\nSearch 25:", "Found" if result else "Not Found")

    # Delete
    root = avl.delete(root, 30)
    print("\nInorder after deleting 30:")
    avl.inorder(root)
```

---

**How This Works**

**Insert**
- Works like BST
- After insertion:
    - Update height
    - Check balance
    - Perform rotation if needed

**Delete**
- Works like BST delete
- Then rebalance using same logic


**Rotations**
- LL → Right rotate
- RR → Left rotate
- LR → Left + Right
- RL → Right + Left

---

**Sample Output**

```
Inorder Traversal:
10 20 25 30 40 50

Preorder Traversal:
30 20 10 25 40 50

Search 25: Found

Inorder after deleting 30:
10 20 25 40 50
```

---
