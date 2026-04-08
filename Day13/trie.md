# Trie (Prefix Tree) Data Structure

## Overview

A **Trie** (pronounced "try") is a tree-based data structure optimized for storing and searching strings efficiently, especially for prefix-based queries.

### Real-World Analogy

Just like words in a dictionary are grouped by common prefixes, a Trie organizes strings hierarchically:
- Words: `cat`, `car`, `care` all start with `ca`

```
    (root)
      |
      c
      |
      a
     / \
    t   r
        |
        e
```

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Node** | Represents a single character |
| **Path** | Sequence from root to node forms a word |
| **isEnd Flag** | Marks the end of a valid word |
| **Children Dict** | Maps characters to child nodes |

---

## Operations

### 1. Insert a Word

**Objective:** Store a word in the Trie

**Steps:**
1. Start at the root node
2. For each character in the word:
   - If child node doesn't exist, create it
   - Move to child node
3. Mark the final node as end-of-word

**Example:** Insert `"cat"`
```
Start: root → c → a → t (mark as end)
```

### 2. Search a Word

**Objective:** Check if a complete word exists

**Steps:**
1. Start at the root node
2. For each character, check if child exists:
   - If not found, return `False`
   - Move to child node
3. At the end, verify `isEnd == True`

**Example:** Search `"cat"` → Returns `True` (if word exists)

### 3. Prefix Search

**Objective:** Check if any word starts with a prefix

**Steps:**
1. Start at the root node
2. For each character in prefix, check if path exists
3. If complete path found, return `True` (no need to check `isEnd`)

**Example:** Search prefix `"ca"` → Returns `True` (matches `cat`, `car`, `care`)

### 4. Delete a Word

**Objective:** Remove a word from the Trie

**Steps:**
1. Start at the root node
2. Traverse to the end of the word, tracking the path
3. Mark the final node's `isEnd` flag as `False`
4. Backtrack from end to start:
   - If a node has no children and `isEnd == False`, delete it
   - Stop if you encounter a node with `isEnd == True` or other children

**Example:** Delete `"cat"` (keeping `"car"`)
```
Before: root → c → a → {t(end), r(end) → e(end)}
After:  root → c → a → {r(end) → e(end)}
        (t node deleted)
```

---

## Python Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}   # Maps character to child TrieNode
        self.isEnd = False   # True if this node marks end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the Trie - O(m) where m is word length"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """Search for exact word - O(m) time"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """Check if any word starts with prefix - O(m) time"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def delete(self, word: str) -> bool:
        """Delete a word from Trie - O(m) time"""
        def _delete_helper(node, word, index):
            if index == len(word):
                # Word doesn't exist
                if not node.isEnd:
                    return False
                node.isEnd = False
                # Return True if node has no children (can be deleted)
                return len(node.children) == 0
            
            ch = word[index]
            if ch not in node.children:
                return False
            
            child_node = node.children[ch]
            should_delete_child = _delete_helper(child_node, word, index + 1)
            
            if should_delete_child:
                del node.children[ch]
                # Return True if current node can be deleted
                return len(node.children) == 0 and not node.isEnd
            
            return False
        
        return _delete_helper(self.root, word, 0)
```

---

## Usage Examples

```python
# Create and populate Trie
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("care")

# Search operations
print(trie.search("cat"))      # True
print(trie.search("can"))      # False
print(trie.startsWith("ca"))   # True

# Deletion
trie.delete("cat")
print(trie.search("cat"))      # False
print(trie.search("car"))      # True (unaffected)
```

---

## Performance & Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Insert | O(m) | O(m) |
| Search | O(m) | - |
| Prefix Search | O(m) | - |
| Delete | O(m) | - |

*where m = length of word/prefix*

---

## Pros & Cons

### Advantages
- Very fast word and prefix searches
- Automatic alphabetical ordering
- Efficient for dictionary and auto-complete applications
- Scales well with large datasets

### Disadvantages
- Higher memory usage than hash tables
- Slower for single word lookups on small datasets
- Complex implementation compared to arrays/lists

---

## Real-World Applications

| Use Case | Example |
|----------|---------|
| **Auto-complete** | Google search suggestions |
| **Contact Search** | Mobile phone contacts |
| **Spell Checker** | Word validation |
| **IP Routing** | Network routing tables |
| **Dictionary** | Word lookup with prefix support |
| **Game Dev** | Word games (Scrabble, Crossword) |
