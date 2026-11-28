# 110. Balanced Binary Tree

## Problem

- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree)

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
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None) -> Tuple[bool, int]:
            if node is None:
                return (True, 0)

            is_left_balanced, left_height = dfs(node=node.left)
            is_right_balanced, right_height = dfs(node=node.right)

            is_balanced = False
            height = max(left_height, right_height) + 1
            if (
                is_left_balanced
                and is_right_balanced
                and right_height >= left_height-1
                and right_height <= left_height+1
            ):
                is_balanced = True

            return (is_balanced, height)


        return dfs(node=root)[0]

```

- Time complexity is O(N).
- Space complexity is O(N).

### 2. Iteration

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        stack, visited, heights = [root], set(), {}
        while stack:
            node = stack.pop()
            if (
                (node.left is None and node.right is None)
                or (node.left in visited or node.right in visited)
            ):
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)
                if abs(left-right) > 1:
                    return False
                heights[node] = max(left, right) + 1
                visited.add(node)
                continue

            stack.append(node)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return True

```

- Time complexity is O(N).
- Space complexity is O(N).
