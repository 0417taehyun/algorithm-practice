# 145. Binary Tree Postorder Traversal

## Problem

- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal)

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
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []


        def dfs(node: TreeNode | None):
            if node is None:
                return

            dfs(node=node.left)
            dfs(node=node.right)
            answer.append(node.val)


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
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []
        if root is None:
            return answer

        stack, last_visited_node = [root], None
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                answer.append(node.val)
                last_visited_node = node
                continue

            if (
                (node.left is not None and node.left is last_visited_node)
                or (node.right is not None and node.right is last_visited_node)
            ):
                answer.append(node.val)
                last_visited_node = node
                continue

            stack.append(node)
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
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []
        node = root
        while node is not None:
            if node.right is None:
                answer.append(node.val)
                node = node.left
                continue

            leftmost = node.right
            while leftmost.left is not None and leftmost.left is not node:
                leftmost = leftmost.left

            if leftmost.left is node:
                leftmost.left = None
                node = node.left
            else:
                answer.append(node.val)
                leftmost.left = node
                node = node.right

        answer.reverse()
        return answer

```

- Time complexity is O(N).
- Space complexity is O(1).
