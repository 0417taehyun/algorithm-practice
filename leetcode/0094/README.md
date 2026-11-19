# 94. Binary Tree Inorder Traversal

## Problem

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)

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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []


        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return None

            inorder(node=node.left)
            answer.append(node.val)
            inorder(node=node.right)


        inorder(node=root)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Using Stack

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer, stack, node = [], [], root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            answer.append(node.val)
            node = node.right

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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
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

            if rightmost.right is None:
                rightmost.right = node
                node = node.left
            else:
                rightmost.right = None
                answer.append(node.val)
                node = node.right

        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
