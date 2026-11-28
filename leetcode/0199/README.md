# 199. Binary Tree Right Side View

## Problem

- [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)

## Solution

### 1. Breadth-Search First

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        answer = []
        queue = deque()
        if root is not None:
            queue.append(root)

        while queue:
            size = len(queue)
            for idx in range(size):
                node = queue.popleft()
                if idx == size-1:
                    answer.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return answer
```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Depth-Search First

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        answer = []


        def dfs(node: TreeNode | None, depth: int) -> None:
            if node is None:
                return

            if len(answer) == depth:
                answer.append(node.val)

            dfs(node=node.right, depth=depth+1)
            dfs(node=node.left, depth=depth+1)


        dfs(node=root, depth=0)
        return answer

```

- Time complexity is O(N).
- Space complexity is O(N).
