# 173. Binary Search Tree Iterator

## Problem

- [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator)

## Solution

### 1. Using Stack

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        node, stack = root, []
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            self.values.append(node.val)
            node = node.left

    def next(self) -> int:
        return self.values.pop()

    def hasNext(self) -> bool:
        return len(self.values) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

> Both next and hasNext function take O(1) time complexity, and N refers the number of function calls.

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Space Optimization

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.subtree = []
        self._retrieve_leftmost_subtree(node=root)

    def _retrieve_leftmost_subtree(self, node: TreeNode) -> None:
        while node is not None:
            self.subtree.append(node)
            node = node.left

    def next(self) -> int:
        node = self.subtree.pop()
        if node.right is not None:
            self._retrieve_leftmost_subtree(node=node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.subtree) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

> H refers height

- Time complexity is O(N).
- Space complexity is O(H).
