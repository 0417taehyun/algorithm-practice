# 701. Insert into a Binary Search Tree

## Problem

- [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree)

## Solution

### 1. Recursion

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val=val)

        if root.val > val:
            root.left = self.insertIntoBST(root=root.left, val=val)
        else:
            root.right = self.insertIntoBST(root=root.right, val=val)

        return root

```

> H refers the maximum height of the tree

- Time complexity is O(H).
- Space complexity is O(H).

### 2. Iteration

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        node = root
        while node is not None:
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val=val)
                    return root
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val=val)
                    return root
                node = node.right

        # root is None
        return TreeNode(val=val)

```

> H refers the maximum height of the tree

- Time complexity is O(H).
- Space complexity is O(1).
