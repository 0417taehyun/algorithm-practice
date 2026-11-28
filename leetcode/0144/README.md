# 144. Binary Tree Preorder Traversal

## Problem

- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal)

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
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []


        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return

            answer.append(node.val)
            dfs(node=node.left)
            dfs(node=node.right)


        dfs(node=root)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Iteration using Stack

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []
        if root is None:
            return answer

        stack = [root]
        while stack:
            node = stack.pop()
            answer.append(node.val)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).

### 3. Morris Traversal

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []
        node = root
        while node is not None:
            if node.left is None:
                answer.append(node.val)
                node = node.right
                continue

            rightmost = node.left
            while rightmost.right is not None and rightmost.right is not node:
                rightmost = rightmost.right

            if rightmost.right is node:
                rightmost.right = None
                node = node.right
            else:
                answer.append(node.val)
                rightmost.right = node
                node = node.left

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
