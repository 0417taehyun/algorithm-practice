# 1120. Maximum Average Subtree

## Problem

- [1120. Maximum Average Subtree](https://leetcode.com/problems/maximum-average-subtree/)

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
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # Return (size, sum, max)
        def dfs(node: Optional[node], size: int) -> Tuple[int, int, int]:
            if node is None:
                return (0, 0, 0)

            total_size = 1
            total_sum = node.val

            left_max = 0
            if node.left is not None:
                left_size, left_sum, left_max = dfs(node=node.left, size=size)
                total_size += left_size
                total_sum += left_sum

            right_max = 0
            if node.right is not None:
                right_size, right_sum, right_max = dfs(node=node.right, size=size)
                total_size += right_size
                total_sum += right_sum

            max_avg = max(total_sum/total_size, left_max, right_max)

            return (total_size, total_sum, max_avg)


        return dfs(node=root, size=0)[2]

```

- Time complexity is O(N).
- Space complexity is O(N).
