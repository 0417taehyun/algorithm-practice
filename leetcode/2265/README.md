# 2265. Count Nodes Equal to Average of Subtree

## Problem

- [2265. Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree)

## Solution

### 1. Depth First Search (DFS)

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Return (size, sum, answer)
        def dfs(node: TreeNode, size: int) -> Tuple[int, int, int]:
            # Leaf node
            if node.left is None and node.right is None:
                return (size+1, node.val, 1)

            answer = 0
            total_size = 1
            total_value = node.val

            # Left subtree
            if node.left is not None:
                left_size, left_value, left_answer = dfs(node=node.left, size=size)

                total_size += left_size
                total_value += left_value
                answer += left_answer

            # Right subtree
            if node.right is not None:
                right_size, right_value, right_answer = dfs(node=node.right, size=size)

                total_size += right_size
                total_value += right_value
                answer += right_answer

            if node.val == (total_value // total_size):
                answer += 1

            return (total_size, total_value, answer)


        return dfs(node=root, size=0)[2]

```

- Time complexity is O(N).
- Space complexity is O(N).
