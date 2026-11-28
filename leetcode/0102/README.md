# 102. Binary Tree Level Order Traversal

## Problem

- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)

## Solution

### 1. Breadth-First Search

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        answer = []
        queue = deque()
        if root is not None:
            queue.append(root)

        while queue:
            nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            answer.append(nodes)

        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Depth-First Search

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        answer = []


        def dfs(node: TreeNode | None, depth: int) -> None:
            if node is None:
                return

            if len(answer) == depth:
                answer.append([])

            answer[depth].append(node.val)
            dfs(node=node.left, depth=depth+1)
            dfs(node=node.right, depth=depth+1)


        dfs(node=root, depth=0)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
