# 450. Delete Node in a BST

## Problem

- [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst)

## Solution

### 1.

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def find_minimum_node(root: TreeNode) -> TreeNode:
            while root is not None and root.left is not None:
                root = root.left
            return root


        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root=root.left, key=key)
        elif root.val < key:
            root.right = self.deleteNode(root=root.right, key=key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            swap_target = find_minimum_node(root=root.right)
            root.val = swap_target.val
            root.right = self.deleteNode(root=root.right, key=swap_target.val)

        return root

```

- Time complexity is O(H).
- Space complexity is O(H).
