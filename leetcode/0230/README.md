# 230. Kth Smallest Element in a BST

## Problem

- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst)

## Solution

### 1. Iterating using Stack

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        node, stack = root, []
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Recursion

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        def dfs(node: TreeNode | None, k: int) -> Tuple[int, int]:
            if node is None:
                return (k, -1)

            left_k, left_val = dfs(node=node.left, k=k)
            if left_k == 0:
                return (0, left_val)

            left_k -= 1
            if left_k == 0:
                return (0, node.val)

            return dfs(node=node.right, k=left_k)


        return dfs(node=root, k=k)[1]

```

- Time complexity is O(N).
- Space complexity is O(N).

### Morris Traversal

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        node = root
        while node is not None:
            if node.left is None:
                k -= 1
                if k == 0:
                    return node.val
                node = node.right
                continue

            rightmost = node.left
            while rightmost.right is not None and rightmost.right is not node:
                rightmost = rightmost.right

            if rightmost.right is node:
                rightmost.right = None
                k -= 1
                if k == 0:
                    return node.val
                node = node.right

            else:
                rightmost.right = node
                node = node.left

```

- Time complexity is O(N).
- Space complexity is O(1).
